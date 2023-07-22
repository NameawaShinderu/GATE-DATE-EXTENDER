import sqlite3

# Step 2: Insert data into the SQLite database
def insert_data_into_database(data_list):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    for item in data_list:
        cursor.execute('INSERT INTO my_table (subs, lecs, dates) VALUES (?, ?, ?)', item)

    connection.commit()
    connection.close()

data_to_insert = [
    ('Basics of network, PYQ', 'L1- 15', 'July 28 - July 30'),
    ('Theorems', 'L16- 26', 'July 31 - August 02'),
    ('PYQ', '', 'August 03'),
    ('Two port network', 'L27- 31', 'August 04'),
    ('PYQ', '', 'August 05'),
    ('Transient', 'L32- 47', 'August 06 - August 08'),
    ('PYQ', '', 'August 09'),
    ('AC', 'L48- 62', 'August 10 - August 12'),
    ('PYQ', '', 'August 13'),
    ('Magnetically coupled', 'L63- 67', 'August 14'),
    ('PYQ', '', 'August 14'),
    ('Basics of Signals', 'L1- 19', 'August 15 - August 18'),
    ('System', 'L20- 24', 'August 19'),
    ('PYQ', '', 'August 20'),
    ('LTI', 'L25- 31', 'August 21 - August 22'),
    ('PYQ', '', 'August 23'),
    ('FS', 'L32- 39', 'August 24 - August 25'),
    ('PYQ', '', 'August 26'),
    ('FT', 'L40- 46', 'August 27 - August 28'),
    ('PYQ', '', 'August 29'),
    ('Sampling', 'L47- 49', 'August 30'),
    ('PYQ', '', 'August 30'),
    ('LT', 'L50-54', 'August 31'),
    ('PYQ', '', 'September 01'),
    ('DTFT', 'L55- 57', 'September 02'),
    ('PYQ', '', 'September 03'),
    ('ZT', 'L58- 60', 'September 04'),
    ('PYQ', '', 'September 05'),
    ('DFT', '', 'September 06'),
    ('PYQ', '', 'September 07'),
    ('Network main notes revision', '', 'September 08 - September 09'),
    ('Basics', 'L1- 3', 'September 10'),
    ('PYQ', '', 'September 10'),
    ('BD & SFG', 'L4- 11', 'September 11 - September 12'),
    ('PYQ', '', 'September 13'),
    ('Time response analysis', 'L12- 22', 'September 14 - September 16'),
    ('PYQ', '', 'September 17'),
    ('RH', 'L23- 28', 'September 18 - September 19'),
    ('PYQ', '', 'September 20'),
    ('Root', 'L29- 34', 'September 21 - September 22'),
    ('PYQ', '', 'September 23'),
    ('Bode', 'L35- 41', 'September 24 - September 25'),
    ('PYQ', '', 'September 26'),
    ('Polar', 'L42- 51', 'September 27 - September 29'),
    ('PYQ', '', 'September 30'),
    ('State state analysis', 'L52- 56', 'October 01'),
    ('PYQ', '', 'October 02'),
    ('Controller', 'L57- 59', 'October 03'),
    ('PYQ', '', 'October 03'),
    ('Signals main notes revision', '', 'October 04 - October 05'),
    ('Network main notes revision', '', 'October 06 - October 07'),
    ('Diode', 'L1- 6', 'October 08 - October 09'),
    ('Clipper', 'L7- 12', 'October 10 - October 11'),
    ('Clamper', 'L13- 22', 'October 12 - October 13'),
    ('Rectifier', 'L23- 31', 'October 14 - October 15'),
    ('Filter', 'L34- 43', 'October 16 - October 17'),
    ('Regulator', 'L44- 53', 'October 18 - October 19'),
    ('PYQ of Diodes', '', 'October 20 - October 21'),
    ('BJT', 'L23- 42', 'October 21 - October 24'),
    ('Freq. response BJT', 'L43- 53', 'October 25 - October 27'),
    ('PYQ of BJT', '', 'October 28'),
    ('JFET', 'L54- 60', "Don't do"),
    ('MOSFET', 'L62- 75', 'October 29 - October 31'),
    ('PYQ of Mosfet', '', 'November 01'),
    ('Op-amp.', 'L76- 92', 'November 02 - November 05'),
    ('PYQ', '', 'November 06'),
    ('Oscillators', 'L93- 99', "Don't do"),
    ('Control main notes revision', '', 'November 07 - November 08'),
    ('Signals main notes revision', '', 'November 09 - November 10'),
    ('Network main notes revision', '', 'November 11')
]


# Call the function to insert data into the database
insert_data_into_database(data_to_insert)
