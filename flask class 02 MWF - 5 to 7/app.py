from flask import Flask , render_template , request   # type: ignore 

app = Flask(__name__) # type: ignore

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return "<h1>about</h1>"

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/user/<name>")
def userName(name):
    return render_template("user.html" , YourName=name)

@app.route("/success" , methods=["GET" , "POST" ])
def success():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        course = data["course"]
        record = {name: "name" , "course" : course }
    return render_template("user.html" , record = record )


app.run(debug=True)