from flask import Flask, redirect,url_for,render_template,request,session,flash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key='A?Y2$W-N+~A.+bqt'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/content/")
def content():
    return render_template('content.html')

@app.route("/katz/")
def katz():
    return render_template('katz.html')
@app.route("/sora/")
def sora():
    return render_template('sora.html')

@app.route("/combine/")
def combine():
    return render_template('combine.html')
if __name__ == '__main__':
    app.run(debug=True)