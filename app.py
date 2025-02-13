from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return render_template("prediction.html")

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    q = float(request.form.get("q"))
    return render_template("dbs.html", r=(-50.6*q)+90.2)

if __name__ == "__main__":
    app.run()

