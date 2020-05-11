from flask import Flask, request, render_template
import os
import requests
from openpyxl import Workbook
# import xlrd
import csv
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        rawData = request.files['rawFile'].read().decode('utf-8').split("\n")  # string
        data = []

        for row_data in rawData:
            if len(row_data) is not 0:
                raw_data = row_data.split(" ")

                url = "https://neelpatel05.pythonanywhere.com/element/atomicnumber"
                payload = {'atomicnumber': raw_data[0]}
                element_data = requests.get(url, params=payload).json()
                print("element_data")
                print(element_data)

                export_data = raw_data
                export_data[0] = element_data['symbol']
                print("export_data")
                print(export_data)
                data.append(export_data)
        print(data)

        new_data = pd.DataFrame(data, columns=['element', 'x', 'y', 'z']).set_index('element')
        new_data.to_csv("test.csv", sep=',')

    # return render_template('index.html')


if __name__ == '__main__':
    app.run()
