from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    age = request.form['age']

    try:
        age = int(age)
        if age >= 18:
            return redirect(url_for('result', name=name, age=age))
        else:
            return redirect(url_for('error'))
    except ValueError:
        return redirect(url_for('error'))

@app.route('/result/<name>/<int:age>')
def result(name, age):
    return render_template('result.html', name=name, age=age)

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
