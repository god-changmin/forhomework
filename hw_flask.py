from flask import Flask
app = Flask(__name__)
@app.router("/")
def helloworld():
    return "Hello world"

if __name__ =="__mail__"
    app.run(host="0.0.0.0")