from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def store_data(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        name = data['name']
        msg = data['message']
        file = database.write(f'{email}, {name}, {msg}')

def store_data_csv(data):
    with open('database.csv', mode='a', newline='') as databaseCsv:
        email = data['email']
        name = data['name']
        msg = data['message']
        csv_file = csv.writer(databaseCsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, name, msg])

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            store_data_csv(data)
            return render_template('thank_you.html', form_data=data)
        except:
            return 'There was an error processing your form. Please try again.'

    return 'error! try again'
