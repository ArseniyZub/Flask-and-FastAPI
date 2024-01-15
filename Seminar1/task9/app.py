from flask import Flask, render_template

app = Flask(__name__)

@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')

@app.route('/jackets/')
def jackets():
    return render_template('jackets.html')

    
if __name__ == "__main__":
    app.run(debug=True)