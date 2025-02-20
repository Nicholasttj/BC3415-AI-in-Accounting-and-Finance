from flask import Flask
from flask import request,render_template
import textblob

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    q = float(request.form.get("q"))
    return(render_template("dbs.html", r=(-50.6*q)+90.2))

@app.route("/sentiment_analysis",methods=["GET","POST"])
def sentiment_analysis():
    return(render_template("sentiment_analysis.html"))

@app.route("/sentiment_result",methods=["GET","POST"])
def sentiment_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return(render_template("sentiment_result.html", r=r))

if __name__ == "__main__":
    app.run()