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

@app.route("/suma/<int:n1>/<int:n2>")
def suma(n1,n2):
    return "{} + {} = {}".format(n1,n2,n1+n2)

#@app.route("/suma/<string:n1>/<string:n2>")
#def suma3(n1,n2):
#    n1=is_number(n1)
#    n2=is_number(n2)
#    if(n1!=False and n2=!=False):
#        return "{} + {} = {}".format(n1,n2,n1+n2)
    
@app.route("/suma/<int:n1>/<int:n2>/json")
def suma2(n1,n2):
    resultado=n1/n2   
    return jsonify(operacion="Suma",FirstOperand=n1,SecondOperand=n2,result=resultado)


@app.route("/divide/<int:n1>/<int:n2>")
def divide(n1,n2):
    return "{} / {} = {}".format(n1,n2,n1/n2)

@app.route("/divide/<int:n1>/<int:n2>/json")
def divide2(n1,n2):
    resultado=n1/n2
    if(n2==0):
        return jsonify(operacion="division",FirstOperand=n1,SecondOperand=n2,result="OperationError")    
    return jsonify(operacion="division",FirstOperand=n1,SecondOperand=n2,result=resultado)

if __name__ == "__main__":
    #app.run(debug=True,port=3000,host=0.0.0.0)
    app.run(debug=True)

def is_number(s):
    try:
        return float(s)
    except ValueError:
        return False


#error page handler
@app.errorhandler(404):
def error404(error):
    pass  #Render an error template and passes the parameter for the template

