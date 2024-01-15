from flask import Flask, render_template

app = Flask(__name__)

@app.route('/aboutUs/')
def aboutUs():
    context = {
        'tittle': 'About Us'
    }

    return render_template('aboutUs.html', **context)

@app.route('/contacts/')
def contacts():
    stud_list = ({
        'firstname': 'David',
        'lastname': 'Black',
        'age': 25,
        'number': '+79892479785'
    },{    
        'firstname': 'David2',
        'lastname': 'Black2',
        'age': 26,
        'number': '+79892479726'
    },{
        'firstname': 'David3',
        'lastname': 'Black3',
        'age': 27,
        'number': '+79892479792'
    })

    return render_template('contacts.html', stud_list=stud_list)

if __name__ == "__main__":
    app.run(debug=True)