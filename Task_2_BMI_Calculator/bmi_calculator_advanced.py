# TASK 2 · BMI Calculator

# Objective: Build a Python program that calculates a user's Body Mass Index (BMI) and classifies it into health categories. Beginners build a command-line tool; advanced builds a full GUI application with data persistence and trend visualisation.

# Tech Stack — Advanced: Python, tkinter or PyQt5, matplotlib, sqlite3 or CSV file storage


# Feature Checklist — Advanced Tier (includes all Beginner features, plus):
# [ ] GUI window built with tkinter or PyQt5 — no command line
# [ ] Input fields with labels for weight and height; a "Calculate" button
# [ ] Result displayed in the GUI with colour-coded feedback (e.g., green = normal, red = obese)
# [ ] Multi-user support: allow saving BMI records for different named users
# [ ] Historical records stored in an SQLite database or CSV file
# [ ] Graph view: display a line chart of a user's BMI trend over time using matplotlib
# [ ] Error handling for database read/write failures

# For the advanced tier, search "Python tkinter GUI tutorial beginners" and "Python matplotlib line chart tutorial". Reference the official tkinter documentation (docs.python.org) for widget layouts. For SQLite, search "Python sqlite3 tutorial CRUD".

## ADVANCED ##

import tkinter as tk
from tkinter import ttk
import sqlite3
import datetime
import matplotlib.pyplot as plt


# Creating database function

def create_database():
    connection = sqlite3.connect("bmi_records.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL
        )
    """)

    cursor.execute("PRAGMA table_info(bmi_records)")
    columns = cursor.fetchall()

    column_names = [column[1] for column in columns]

    if "date_time" not in column_names:
        cursor.execute("""
            ALTER TABLE bmi_records
            ADD COLUMN date_time TEXT
        """)

    connection.commit()
    connection.close()


# BMI catagory function

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Under weight", "blue"

    elif bmi <= 24.9:
        return "Normal", "green"

    elif bmi <= 29.9:
        return "Over weight", "orange"

    else:
        return "Obese", "red"

# Creating function for calculation & output

def calculate_bmi():
    try:
        name = name_entry.get().strip()

        if not name:
            result_label.config(
                text="Enter your name",
                fg="red"
            )
            return


        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            result_label.config(
                text="Weight and height must be greater than 0",
                fg="red"
            )
            return

        

    except ValueError:
        result_label.config(
            text="Please enter numbers only",
            fg="red"
        )
        return

    bmi = weight / (height**2)

    category, result_color = get_bmi_category(bmi)
    date_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

# Data records storing

    try:
        connection = sqlite3.connect("bmi_records.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO bmi_records
        (name, weight, height, bmi, category, date_time)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, weight, height, bmi, category, date_time))

        connection.commit()
        connection.close()

    except sqlite3.Error as error:
        result_label.config(
        text="Database error!\nRecord was not saved.",
        fg="red"
        )
        print("Database error:", error)
        return
    
    result_label.config(
        text=f"BMI: {round(bmi, 2)}\nCategory: {category}",
        fg=result_color
    )


create_database()   


# History function


def show_history():
    history_window = tk.Toplevel(window)
    history_window.title("BMI History")
    history_window.geometry("900x500")

    history_label = tk.Label(
        history_window,
        text="BMI HISTORY",
        font=("Times New Roman", 18, "bold")
    )
    history_label.pack(pady=15)

    table_frame = tk.Frame(history_window)
    table_frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=10
    )

    columns = ("Name", "Weight", "Height", "BMI", "Category", "Date/Time")

    history_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    history_table.heading("Name", text="Name")
    history_table.heading("Weight", text="Weight (kg)")
    history_table.heading("Height", text="Height (m)")
    history_table.heading("BMI", text="BMI")
    history_table.heading("Category", text="Category")
    history_table.heading("Date/Time", text="Date/Time")

    history_table.column("Name", width=150, anchor="center")
    history_table.column("Weight", width=150, anchor="center")
    history_table.column("Height", width=150, anchor="center")
    history_table.column("BMI", width=150, anchor="center")
    history_table.column("Category", width=180, anchor="center")
    history_table.column("Date/Time", width=180, anchor="center")

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=history_table.yview
    )

    history_table.configure(
        yscrollcommand=scrollbar.set
    )

    history_table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    try:
        connection = sqlite3.connect("bmi_records.db")
        cursor = connection.cursor()

        cursor.execute("""
        SELECT name, weight, height, bmi, category, date_time
        FROM bmi_records
        """)

        records = cursor.fetchall()
        connection.close()

    except sqlite3.Error as error:
        error_label = tk.Label(
            history_window,
            text="Database error!\nCould not read BMI records.",
            fg="red"
        )
        error_label.pack(pady=20)

        print("Database error:", error)
        return

    for record in records:
        history_table.insert(
            "",
            "end",
            values=(
                record[0],
                record[1],
                record[2],
                round(record[3], 2),
                record[4],
                record[5]
            )
        )



# BMI trend function for graph

def show_bmi_trend():
    name = name_entry.get().strip()

    if not name:
        result_label.config(
            text="Enter a name to view BMI trend",
            fg="red"
        )
        return

    try:
        connection = sqlite3.connect("bmi_records.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT bmi, date_time
            FROM bmi_records
            WHERE name = ?
            AND date_time IS NOT NULL
            AND date_time != ''
            ORDER BY date_time
        """, (name,))

        records = cursor.fetchall()
        connection.close()

        if not records:
            result_label.config(
                text=f"No BMI records found for {name}",
                fg="red"
            )
            return

        dates = []
        bmi_values = []

        for bmi, date_time in records:
            date_object = datetime.datetime.strptime(
                date_time,
                "%d-%m-%y %H:%M:%S"
            )

            dates.append(date_object)
            bmi_values.append(bmi)


        plt.figure(figsize=(8, 5))

        plt.plot(
            dates,
            bmi_values,
            marker="o"
        )

        plt.title(f"BMI Trend - {name}")
        plt.xlabel("Date and Time")
        plt.ylabel("BMI")

        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()



    except sqlite3.Error as error:
        result_label.config(
            text="Database error!\nCould not read BMI records.",
            fg="red"
        )
        print("Database error:", error)
        return


# Main Window created

window = tk.Tk()

window.title("BMI Calculator")
window.geometry("400x600")

title_label = tk.Label(
    window,
    text="BMI CALCULATOR",
    font=("Times New Roman", 20, "bold")
)

title_label.pack(pady=20)

# Multi-User name entry

name_label = tk.Label(
    window,
    text="Name:"
)

name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack(pady=5)

# Weight entery box created in main window

weight_label = tk.Label(
    window,
    text="Weight (kg):"
)

weight_label.pack()

weight_entry = tk.Entry(window)

weight_entry.pack(pady=5)

# height entery box created in main window

height_label = tk.Label(
    window,
    text="Height (m):"
)

height_label.pack()

height_entry = tk.Entry(window)

height_entry.pack(pady=5)

# Calculate button created in main window

calculate_button = tk.Button(
    window,
    text="Calculate",
    command = calculate_bmi
)

calculate_button.pack(pady=10)

# Result label creating in main window

result_label = tk.Label(
    window,
    text= "BMI: --" "\n""Category: --" ,
    font=("Times New Roman", 15)

)
result_label.pack(pady= 10)


# History button

history_button = tk.Button(
    window,
    text="History",
    command=show_history
)

history_button.pack(pady=5)

# trend graph button

trend_button = tk.Button(
    window,
    text="BMI Trend",
    command=show_bmi_trend
)
trend_button.pack(pady=5)


window.mainloop()