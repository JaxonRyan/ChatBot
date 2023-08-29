import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Read user login details from the CSV file
def read_users_from_csv():
    users = {}
    with open('Year 12 - Sheet1.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users[row['username']] = row['password']
    return users


users = read_users_from_csv()


# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect(url_for('home'))  # Corrected redirection
        else:
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)

    return render_template('login.html', error=None)


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)


