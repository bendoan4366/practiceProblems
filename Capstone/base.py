from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:P1usUltr@!@localhost/tutorial'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route('/')
def home():
    return render_template("home.html")



@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email"]
        user_name = request.form["name"]
        user_height = request.form["message"]
        # print(request.form)
        # print("UN: " + user_name + " //Email: " + email + " //Height: " + str(user_height))
        return render_template("success.html")



if __name__ == "__main__":
    app.run(debug = True)

