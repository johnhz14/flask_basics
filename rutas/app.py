from flask import Flask 
app = Flask(__name__)

@app.route("/")
def index():
    return "hello World"

@app.route("/hola")
def hola():
    return "hola."

@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "tu numero es {} ".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {}, nombre de usuario: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    resultado = n1 + n2
    return "El resultado de la operacion es:{} ".format(resultado)

@app.route("/default")
@app.route("/default/<string:dft>")
def dft(dft ="xD"):
    return "el valor de dft es " + dft


if __name__ == "__main__":
    #app.run(debug=True,port=3000,host=0.0.0.0)
    app.run(debug=True)
