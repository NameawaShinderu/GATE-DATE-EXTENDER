import sqlite3

# Data to be inserted
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
    ]
# Create and connect to the database
conn = sqlite3.connect("schedule.db")
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedule (
        topic TEXT,
        lecture TEXT,
        date_range TEXT
    )
''')

# Insert data into the table
cursor.executemany('INSERT INTO schedule VALUES (?, ?, ?)', dates)

# Commit changes and close the connection
conn.commit()
conn.close()
import sqlite3
from datetime import datetime

def get_updated_dates(start_date):
    # Convert the user input to a Python date object
    user_date = datetime.strptime(start_date, "%Y-%m-%d")

    conn = sqlite3.connect("schedule.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM schedule")
    data = cursor.fetchall()

    updated_dates = []

    for topic, lecture, date_range in data:
        if date_range:
            date_parts = date_range.split(" - ")
            start_date_str = date_parts[0]
            end_date_str = date_parts[1] if len(date_parts) > 1 else start_date_str

            # Extract the month and day from the start_date_str
            month, day = start_date_str.split("-")
            month_number = datetime.strptime(month, "%b").month

            # Append the year from the user input to the database date strings
            start_date_str_with_year = f"{start_date[:4]}-{month_number:02d}-{day}"
            end_date_str_with_year = f"{start_date[:4]}-{month_number:02d}-{end_date_str}"

            # Convert the database date strings to Python date objects
            db_start_date = datetime.strptime(start_date_str_with_year, "%Y-%m-%d")
            db_end_date = datetime.strptime(end_date_str_with_year, "%Y-%m-%d")

            # Check if the user date falls within the database date range
            if db_start_date <= user_date <= db_end_date:
                if lecture:
                    updated_dates.append((topic, lecture, f"{start_date_str} - {end_date_str}"))
                else:
                    updated_dates.append((topic, "", f"{start_date_str} - {end_date_str}"))
        else:
            # Handle the case where date_range is empty (no dates available)
            updated_dates.append((topic, "", ""))

    conn.close()
    return updated_dates

if __name__ == "__main__":
    user_input = input("Enter the starting date (YYYY-MM-DD): ")

    try:
        updated_dates = get_updated_dates(user_input)
        if updated_dates:
            for topic, lecture, date_range in updated_dates:
                print(f"{topic}, {lecture}, {date_range}")
        else:
            print("No events found after the provided date.")
    except Exception as e:
        print(f"Error: {e}")