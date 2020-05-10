from flask import Flask, request, render_template
import os
import requests
from openpyxl import Workbook
# import xlrd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        rawData = request.files['rawFile'].read()
        print(rawData)
    # else:
    #     return render_template(request, 'index.html')


if __name__ == '__main__':
    app.run()
