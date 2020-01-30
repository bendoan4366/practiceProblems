from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from emailScript import send_email


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:P1usUltr@!@localhost/tutorial'
db = SQLAlchemy(app)

#create a Data class that inherits properties from db.Model (a database model), create table & assign attributes
class Data(db.Model):
    __tablename__ = "capstonedata"
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
        user_email = request.form["email"]
        user_name = request.form["name"]
        user_height = request.form["message"]
        send_email(user_email, user_height)
        # print(request.form)
        # print("UN: " + user_name + " //Email: " + email + " //Height: " + str(user_height))

        #query the table in the Data class, and filter for email attribute only and find email attibute with user's email
        if db.session.query(Data).filter(Data.email_==user_email).count() == 0:
            data = Data(user_email, user_height)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        else: 
            db.session.query(Data).filter(Data.email_==user_email).update({Data.height_:user_height})
            db.session.commit()

    return(render_template('home.html', text = "You already entered that email bruh"))


if __name__ == "__main__":
    app.run(debug = True)

