from flask import Flask, redirect,url_for,render_template,request,session,flash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key='A?Y2$W-N+~A.+bqt'

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)