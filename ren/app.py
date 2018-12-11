from flask import Flask 
from flask import render_template
from flask import jsonify
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/acerca")
def about():
    return render_template("about.html")


@app.route("/suma/<string:n1>/<string:n2>")
def suma(n1,n2):
    try:
        n1=float(n1)
        n2=float(n2)
        return "{} + {} = {}".format(n1,n2,n1+n2)
    except:
        return "Invalid types"
    
@app.route("/suma/<string:n1>/<string:n2>/json")
def suma2(n1,n2):
    try:
        n1=float(n1)
        n2=float(n2)
        resultado=n1/n2
        return jsonify(operacion="Suma",FirstOperand=n1,SecondOperand=n2,result=resultado)
    except:
        return "Invalid types"

@app.route("/divide/<string:n1>/<string:n2>")
def divide(n1,n2):
    try:
        n1=float(n1)
        n2=float(n2)
        resultado=n1/n2
        return "{} + {} = {}".format(n1,n2,resultado)
    except:
        return "Invalid types"
    
@app.route("/suma/<string:n1>/<string:n2>/json")
def divide2(n1,n2):
    try:
        n1=float(n1)
        n2=float(n2)
        resultado=n1/n2
        return jsonify(operacion="Suma",FirstOperand=n1,SecondOperand=n2,result=resultado)
    except:
        return "Invalid types"



if __name__ == "__main__":
    #app.run(debug=True,port=3000,host=0.0.0.0)
    app.run(debug=True)


#error page handler
@app.errorhandler(404)
def error404(error):
    return "----------------PAGE NOT FOUND----------"

