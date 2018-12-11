from flask import Flask 
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/acerca")
def about():
    return render_template("about.html")

@app.route("/suma/<int:n1>/<int:n2>")
def suma(n1,n2):
    return "{} + {} = {}".format(n1,n2,n1+n2)

@app.route("/divide/<int:n1>/<int:n2>")
def divide(n1,n2):
    return "{} / {} = {}".format(n1,n2,n1/n2)

if __name__ == "__main__":
    #app.run(debug=True,port=3000,host=0.0.0.0)
    app.run()

