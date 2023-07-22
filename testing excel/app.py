import openpyxl
from flask import Flask, render_template

app = Flask(__name__)

def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    return data

@app.route('/')
def display_excel_as_webpage():
    file_path = 'your_file_updated.xlsx'  # Replace with the path to your updated Excel file
    data = read_excel(file_path)
    return render_template('excel_page.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
