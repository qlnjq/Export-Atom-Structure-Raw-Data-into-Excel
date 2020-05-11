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
        # rawData = request.files['rawFile'].read()
        # print(rawData)  # byte
        # print(rawData.decode('utf-8'))  # strings
        # rawData2 = "".join(map(chr, rawData))
        # print(rawData2)
        data = []
        reader = csv.reader(request.files['rawFile'].read().decode("utf-8").split('\n'), dialect='excel')
        for row in reader:
            if len(row) is not 0:
                split_row = row[0].split(' ')
                data.append(split_row)
        print(data)

        newData = pd.DataFrame(data, columns=['element', 'x', 'y', 'z']).set_index('element')
        newData.to_csv("test.csv", sep=',')

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
