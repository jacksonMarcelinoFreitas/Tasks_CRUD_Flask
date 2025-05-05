from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/about")
def about():
    return "Sobre"

#garante que somente quando execute o servidor de forma manual, execute em modo debug
if __name__ == "__main__":
    app.run(debug=True) #apenas para dev