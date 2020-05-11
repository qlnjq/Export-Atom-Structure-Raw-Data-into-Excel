from flask import Flask, request, render_template
import os
import requests
import pandas as pd

app = Flask(__name__)
STATIC_DIR = 'static/temp'
app.config['STATIC_DIR'] = STATIC_DIR

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

                export_data = raw_data
                print(export_data)
                export_data[0] = element_data['symbol']
                data.append(export_data)
        print("successfully appended data")
        print(data)

        new_data = pd.DataFrame(data, columns=['element', 'x', 'y', 'z']).set_index('element')
        path_to_save = os.path.join(app.config['STATIC_DIR'], "output.csv")
        new_data.to_csv(path_to_save, sep=',')

    return render_template('index.html', export_file=path_to_save, styles="background-color: blueviolet; color: white; display: block !important")


if __name__ == '__main__':
    app.run()
