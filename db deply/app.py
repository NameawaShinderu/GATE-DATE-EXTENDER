import sqlite3
from datetime import datetime, timedelta
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to increase the dates by a given value
def increase_dates(date_list, increment):
    updated_dates = []
    for date_range in date_list:
        if date_range == "Don't do":
            updated_dates.append(date_range)
            continue
        if '-' in date_range:
            start_date, end_date = date_range.split(' - ')
            start_date = datetime.strptime(start_date, '%B %d')
            end_date = datetime.strptime(end_date, '%B %d')
            date_increment = timedelta(days=increment)
            updated_start_date = start_date + date_increment
            updated_end_date = end_date + date_increment
            updated_date_range = f"{updated_start_date.strftime('%B %d')} - {updated_end_date.strftime('%B %d')}"
        else:
            date = datetime.strptime(date_range, '%B %d')
            date_increment = timedelta(days=increment)
            updated_date_range = (date + date_increment).strftime('%B %d')
        updated_dates.append(updated_date_range)
    return updated_dates

# Step 1: Read data from the SQLite database
def read_data_from_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT subs, lecs, dates FROM my_table')
    data = cursor.fetchall()

    connection.close()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_date_input = request.form['user_date']
        try:
            # Convert the user input to a datetime object
            user_date = datetime.strptime(user_date_input, '%Y-%m-%d')

            # Read data from the database
            data_from_database = read_data_from_database()

            # Define the dataset of dates
            dates = [item[2] for item in data_from_database]

            # Calculate the difference in days
            july_8 = datetime.strptime('July 8', '%B %d')
            difference = (user_date - july_8).days

            # Example usage with the difference as the increment value
            updated_dates = increase_dates(dates, difference)

            # Update data in the database
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()

            for i, date_range in enumerate(updated_dates, start=1):
                cursor.execute('UPDATE my_table SET dates = ? WHERE id = ?', (date_range, i))

            connection.commit()
            connection.close()

            # Read updated data from the database
            updated_data = read_data_from_database()

            return render_template('result.html', data=updated_data)

        except ValueError:
            return render_template('error.html')

    return render_template('index.html')

@app.route('/today', methods=['GET'])
def today():
    try:
        # Get the current date
        current_date = datetime.now().date()

        # Read data from the database
        data_from_database = read_data_from_database()

        # Define the dataset of dates
        dates = [item[2] for item in data_from_database]

        # Calculate the difference in days
        july_8 = datetime.strptime('July 8', '%B %d')
        difference = (current_date - july_8.date()).days

        # Example usage with the difference as the increment value
        updated_dates = increase_dates(dates, difference)

        # Update data in the database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        for i, date_range in enumerate(updated_dates, start=1):
            cursor.execute('UPDATE my_table SET dates = ? WHERE id = ?', (date_range, i))

        connection.commit()
        connection.close()

        # Read updated data from the database
        updated_data = read_data_from_database()

        return render_template('result.html', data=updated_data)

    except ValueError:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
