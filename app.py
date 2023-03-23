from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import os


class CleanCache:

    def __init__(self, directory=None):
        self.clean_path = directory
        if os.listdir(self.clean_path) != list():
            files = os.listdir(self.clean_path)
            for fileName in files:
                os.remove(os.path.join(self.clean_path, fileName))


app = Flask(__name__)


CSV_UPLOAD_FILES = os.path.join('static', 'CSV_UPLOAD_FILES')
app.config['CSV_UPLOAD_FILES'] = CSV_UPLOAD_FILES


@app.after_request
def add_header(resp):
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/csv_file_upload1')
def csv_file_upload1():
    return render_template('csv_file_upload1.html')


@app.route('/csv_file_upload2')
def csv_file_upload2():
    return render_template('csv_file_upload2.html')


@app.route('/upload_to_pd_file', methods=['GET', 'POST'])
def upload_to_pd_file():
    '''csv_file_upload1 method'''
    if request.method == 'POST':
        if os.listdir(app.config['CSV_UPLOAD_FILES']) != list():
            CleanCache(directory=app.config['CSV_UPLOAD_FILES'])

        upload_file = request.files['file']
        # form -> post -> to save in specific folder
        upload_file.save(f'static/CSV_UPLOAD_FILES/{secure_filename(upload_file.filename)}')
        # pandas to_html
        df_file = pd.read_csv(f'static/CSV_UPLOAD_FILES/{secure_filename(upload_file.filename)}').to_html()
        return df_file


@app.route('/file_uploaded_read', methods=['GET', 'POST'])
def file_uploaded_read():
    '''csv_file_upload2 method
        NOT FILE SAVE...'''
    if request.method == 'POST':
        if os.listdir(app.config['CSV_UPLOAD_FILES']) != list():
            CleanCache(directory=app.config['CSV_UPLOAD_FILES'])

        upload_file = request.files['file'].read()
        return upload_file


if __name__ == "__main__":
    if os.listdir(app.config['CSV_UPLOAD_FILES']) != list():
        CleanCache(directory=app.config['CSV_UPLOAD_FILES'])
    app.run(debug=True)

