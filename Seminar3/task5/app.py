import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registration_form.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    birthdate = request.form['birthdate']
    agree = request.form.get('agree')

    if not (name and email and password and confirm_password and birthdate and agree):
        return render_template('registration_form.html', error='All fields are required.')

    if password != confirm_password:
        return render_template('registration_form.html', error='Passwords do not match.')

    try:
        birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y').date()
    except ValueError:
        return render_template('registration_form.html', error='Invalid birthdate format.')

    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
