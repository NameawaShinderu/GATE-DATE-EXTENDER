from flask import Flask, render_template, request
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# Create a SQLite database and table to store the dataset
def create_database_table():
    conn = sqlite3.connect("/home/seminal76/mysite/dataset.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dataset (
            topic TEXT,
            lecture TEXT,
            date_range TEXT
        )
    """)

    conn.commit()
    conn.close()
def clear_dataset_table():
    conn = sqlite3.connect("/home/seminal76/mysite/dataset.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM dataset")

    conn.commit()
    conn.close()

# Insert the dataset into the table
def insert_dataset_into_table():
    # Replace 'dates' list with your dataset
    dates = [
        ("Basics of network, PYQ", "L1- 15", "July 8 - July 10"),
        ("Theorems", "L16- 26", "July 11 - July 13"),
        ("PYQ", "", "Jul-14"),
        ("Two port network", "L27- 31", "Jul-15"),
        ("PYQ", "", "Jul-16"),
        ("Transient", "L32- 47", "July 17 - July 19"),
        ("PYQ", "", "Jul-20"),
        ("AC", "L48- 62", "July 21 - July 23"),
        ("PYQ", "", "Jul-24"),
        ("Magnetically coupled", "L63- 67", "Jul-25"),
        ("PYQ", "", "Jul-25"),
        ("Basics of Signals", "L1- 19", "July 26 - July 29"),
        ("System", "L20- 24", "Jul-30"),
        ("PYQ", "", "Jul-31"),
        ("LTI", "L25- 31", "August 1 - August 2"),
        ("PYQ", "", "Aug-03"),
        ("FS", "L32- 39", "August 4 - August 5"),
        ("PYQ", "", "Aug-06"),
        ("FT", "L40- 46", "August 7 - August 8"),
        ("PYQ", "", "Aug-09"),
        ("Sampling", "L47- 49", "Aug-10"),
        ("PYQ", "", "Aug-10"),
        ("LT", "L50-54", "Aug-11"),
        ("PYQ", "", "Aug-12"),
        ("DTFT", "L55- 57", "Aug-13"),
        ("PYQ", "", "Aug-14"),
        ("ZT", "L58- 60", "Aug-15"),
        ("PYQ", "", "Aug-16"),
        ("DFT", "", "Aug-17"),
        ("PYQ", "", "Aug-18"),
        ("Network main notes revision", "", "August 19 - August 20"),
        ("Basics", "L1- 3", "Aug-21"),
        ("PYQ", "", "Aug-21"),
        ("BD & SFG", "L4- 11", "August 22 - August 23"),
        ("PYQ", "", "Aug-24"),
        ("Time response analysis", "L12- 22", "August 25 - August 27"),
        ("PYQ", "", "Aug-28"),
        ("RH", "L23- 28", "August 29 - August 30"),
        ("PYQ", "", "Aug-31"),
        ("Root", "L29- 34", "September 1 - September 2"),
        ("PYQ", "", "Sep-03"),
        ("Bode", "L35- 41", "September 4 - September 5"),
        ("PYQ", "", "Sep-06"),
        ("Polar", "L42- 51", "September 7 - September 9"),
        ("PYQ", "", "Sep-10"),
        ("State state analysis", "L52- 56", "Sep-11"),
        ("PYQ", "", "Sep-12"),
        ("Controller", "L57- 59", "Sep-13"),
        ("PYQ", "", "Sep-13"),
        ("Signals main notes revision", "", "September 14 - September 15"),
        ("Network main notes revision", "", "September 16 - September 17"),
        ("Diode", "L1- 6", "September 18 - September 19"),
        ("Clipper", "L7- 12", "September 20 - September 21"),
        ("Clamper", "L13- 22", "September 22 - September 23"),
        ("Rectifier", "L23- 31", "September 24 - September 25"),
        ("Filter", "L34- 43", "September 26 - September 27"),
        ("Regulator", "L44- 53", "September 28 - September 29"),
        ("PYQ of Diodes", "", "September 30 - October 1"),
        ("BJT", "L23- 42", "October 1 - October 4"),
        ("Freq. response BJT", "L43- 53", "October 5 - October 7"),
        ("PYQ of BJT", "", "Oct-08"),
        ("JFET", "L54- 60", "Don't do"),
        ("MOSFET", "L62- 75", "October 9 - October 11"),
        ("PYQ of Mosfet", "", "Oct-12"),
        ("Op- amp.", "L76- 92", "October 13 - October 16"),
        ("PYQ", "", "Oct-17"),
        ("Oscillators", "L93- 99", "Don't do"),
        ("Control main notes revision", "", "October 18 - October 19"),
        ("Signals main notes revision", "", "October 20 - October 21"),
        ("Network main notes revision", "", "Oct-22")
        # ... (Your dataset here)
    ]

    conn = sqlite3.connect("/home/seminal76/mysite/dataset.db")
    cursor = conn.cursor()

     # Truncate the table before inserting the dataset
    cursor.execute("DELETE FROM dataset")

    for item in dates:
        cursor.execute("INSERT INTO dataset (topic, lecture, date_range) VALUES (?, ?, ?)", item)

    conn.commit()
    conn.close()

# Function to calculate the date difference and update the dates in the dataset
def update_dates_in_dataset(input_date):

    input_date = datetime.strptime(input_date, "%Y-%m-%d")

    
    # Replace 'dates' list with your dataset
    dates = [
        ("Basics of network, PYQ", "L1- 15", "July 8 - July 10"),
        ("Theorems", "L16- 26", "July 11 - July 13"),
        ("PYQ", "", "Jul-14"),
        ("Two port network", "L27- 31", "Jul-15"),
        ("PYQ", "", "Jul-16"),
        ("Transient", "L32- 47", "July 17 - July 19"),
        ("PYQ", "", "Jul-20"),
        ("AC", "L48- 62", "July 21 - July 23"),
        ("PYQ", "", "Jul-24"),
        ("Magnetically coupled", "L63- 67", "Jul-25"),
        ("PYQ", "", "Jul-25"),
        ("Basics of Signals", "L1- 19", "July 26 - July 29"),
        ("System", "L20- 24", "Jul-30"),
        ("PYQ", "", "Jul-31"),
        ("LTI", "L25- 31", "August 1 - August 2"),
        ("PYQ", "", "Aug-03"),
        ("FS", "L32- 39", "August 4 - August 5"),
        ("PYQ", "", "Aug-06"),
        ("FT", "L40- 46", "August 7 - August 8"),
        ("PYQ", "", "Aug-09"),
        ("Sampling", "L47- 49", "Aug-10"),
        ("PYQ", "", "Aug-10"),
        ("LT", "L50-54", "Aug-11"),
        ("PYQ", "", "Aug-12"),
        ("DTFT", "L55- 57", "Aug-13"),
        ("PYQ", "", "Aug-14"),
        ("ZT", "L58- 60", "Aug-15"),
        ("PYQ", "", "Aug-16"),
        ("DFT", "", "Aug-17"),
        ("PYQ", "", "Aug-18"),
        ("Network main notes revision", "", "August 19 - August 20"),
        ("Basics", "L1- 3", "Aug-21"),
        ("PYQ", "", "Aug-21"),
        ("BD & SFG", "L4- 11", "August 22 - August 23"),
        ("PYQ", "", "Aug-24"),
        ("Time response analysis", "L12- 22", "August 25 - August 27"),
        ("PYQ", "", "Aug-28"),
        ("RH", "L23- 28", "August 29 - August 30"),
        ("PYQ", "", "Aug-31"),
        ("Root", "L29- 34", "September 1 - September 2"),
        ("PYQ", "", "Sep-03"),
        ("Bode", "L35- 41", "September 4 - September 5"),
        ("PYQ", "", "Sep-06"),
        ("Polar", "L42- 51", "September 7 - September 9"),
        ("PYQ", "", "Sep-10"),
        ("State state analysis", "L52- 56", "Sep-11"),
        ("PYQ", "", "Sep-12"),
        ("Controller", "L57- 59", "Sep-13"),
        ("PYQ", "", "Sep-13"),
        ("Signals main notes revision", "", "September 14 - September 15"),
        ("Network main notes revision", "", "September 16 - September 17"),
        ("Diode", "L1- 6", "September 18 - September 19"),
        ("Clipper", "L7- 12", "September 20 - September 21"),
        ("Clamper", "L13- 22", "September 22 - September 23"),
        ("Rectifier", "L23- 31", "September 24 - September 25"),
        ("Filter", "L34- 43", "September 26 - September 27"),
        ("Regulator", "L44- 53", "September 28 - September 29"),
        ("PYQ of Diodes", "", "September 30 - October 1"),
        ("BJT", "L23- 42", "October 1 - October 4"),
        ("Freq. response BJT", "L43- 53", "October 5 - October 7"),
        ("PYQ of BJT", "", "Oct-08"),
        ("JFET", "L54- 60", "Don't do"),
        ("MOSFET", "L62- 75", "October 9 - October 11"),
        ("PYQ of Mosfet", "", "Oct-12"),
        ("Op- amp.", "L76- 92", "October 13 - October 16"),
        ("PYQ", "", "Oct-17"),
        ("Oscillators", "L93- 99", "Don't do"),
        ("Control main notes revision", "", "October 18 - October 19"),
        ("Signals main notes revision", "", "October 20 - October 21"),
        ("Network main notes revision", "", "Oct-22")
        # ... (Your dataset here)
    ]

    
    # Calculate the difference between the input_date and July 8
    reference_date = datetime(year=input_date.year, month=7, day=8)
    date_difference = (input_date - reference_date).days

    # Update the dates in the dataset
    updated_dates = []
    for item in dates:
        if " - " in item[2]:
            # If the date is in the range format "July 8 - July 10"
            start_date_str, end_date_str = item[2].split(" - ")
            start_date = datetime.strptime(start_date_str, "%B %d")
            end_date = datetime.strptime(end_date_str, "%B %d")
            updated_start_date = start_date + timedelta(days=date_difference)
            updated_end_date = end_date + timedelta(days=date_difference)
            updated_date_range = f"{updated_start_date.strftime('%b-%d')} - {updated_end_date.strftime('%b-%d')}"
            updated_dates.append((item[0], item[1], updated_date_range))
        else:
            # If the date is in the single date format "Jul-14" or doesn't have a date range
            date_str = item[2]
            if date_str.lower() == "don't do":
                # Skip entries with "Don't do"
                updated_dates.append(item)
            else:
                date = datetime.strptime(date_str, "%b-%d")
                updated_date = date + timedelta(days=date_difference)
                updated_dates.append((item[0], item[1], updated_date.strftime("%b-%d")))

    # Update the dataset in the database
    conn = sqlite3.connect("/home/seminal76/mysite/dataset.db")
    cursor = conn.cursor()

    # Fetch the existing data from the table
    cursor.execute("SELECT * FROM dataset")
    existing_data = cursor.fetchall()

    # Update the records in the table with the updated dates
    for idx, (_, _, date_range) in enumerate(existing_data):
        if idx < len(updated_dates):
            updated_data = updated_dates[idx]
            cursor.execute("UPDATE dataset SET topic=?, lecture=?, date_range=? WHERE rowid=?", (*updated_data, idx + 1))
        else:
            # If the updated dataset is shorter than the original dataset, break the loop
            break

    conn.commit()
    conn.close()

def update_dates_with_today():
    # Get today's date
    today_date = datetime.today().strftime("%Y-%m-%d")
    # Call the function to update the dataset with today's date
    update_dates_in_dataset(today_date)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input_date = request.form["input_date"]
        # Call the function to update the dataset with the input date
        update_dates_in_dataset(user_input_date)
    
    # Fetch the updated dataset from the database
    conn = sqlite3.connect("/home/seminal76/mysite/dataset.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dataset")
    updated_dates = cursor.fetchall()
    conn.close()

    return render_template("index.html", updated_dates=updated_dates)

@app.route("/today", methods=["GET"])
def today():
    # Call the function to update the dataset with today's date
    update_dates_with_today()

    # Fetch the updated dataset from the database
    conn = sqlite3.connect("/home/seminal76/mysite/dataset.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dataset")
    updated_dates = cursor.fetchall()
    conn.close()

    return render_template("index.html", updated_dates=updated_dates)

if __name__ == "__main__":
    # Create the database and table
    create_database_table()
    # Insert the dataset into the table
    insert_dataset_into_table()

    app.run(debug=True)