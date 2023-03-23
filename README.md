# FLASK-CSV-UPLOAD TESTING
this repository is about csv file upload testing with FLASK.
upload file save and read testing with two different code.
---
## Structure
- static
  - CSV_UPLOAD_FILES
    - (user upload file save here)
- templates
  - index.html
  - csv_file_upload1.html
  - csv_file_upload2.html
- app.py


## UPLOAD & READ Code Sample
- html style table show up in web page

```
    upload_file = request.files['file']
    upload_file.save(f'static/CSV_UPLOAD_FILES/{secure_filename(upload_file.filename)}')
    df_file = pd.read_csv(f'static/CSV_UPLOAD_FILES/{secure_filename(upload_file.filename)}').to_html()
    return df_file
```

- short code, directly read csv items

```commandline
    upload_file = request.files['file'].read()
    return upload_file
```
## ADD 
- Cache Cleaning

---
- 2023-03-23 