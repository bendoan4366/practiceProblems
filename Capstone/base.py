from flask import Flask, render_template, request

app = Flask(__name__)

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
        print(request.form)

        print("UN: " + user_name + " //Email: " + email + " //Height: " + str(user_height))
        return render_template("success.html")

if __name__ == "__main__":
    app.run(debug = True)

