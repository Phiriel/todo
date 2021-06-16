import csv
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.utils import redirect

app = Flask(__name__,template_folder="template", static_folder="styles")

engine = create_engine('postgresql://postgres:Naruto123@localhost:5432/postgres')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=["GET","POST"])
def index():
    students = db.execute("SELECT * FROM todo").fetchall()
    return render_template('list.html',students=students)  

@app.route("/add", methods=["POST","GET"])
def add():
    task=request.form.get("task")
    time=request.form.get("time")
    db.execute("INSERT INTO todo (task,time) VALUES(:task,:time)", {"task":task,"time":time})
    db.commit()
    return redirect("/")

@app.route("/updateform/<int:key>", methods=["GET","POST"])
def form(key):
    return render_template("update.html",key=key) 

@app.route("/update/<int:key>", methods=["GET","POST"])
def update(key):
    newtask=request.form.get("newtask")
    db.execute(f"UPDATE todo SET task=(:task) WHERE id={key}",{"task":newtask})
    db.commit()
    return redirect("/")

@app.route("/delete/<int:key>", methods=["GET","POST"])
def delete(key):
    db.execute(f"DELETE FROM todo WHERE id={key}")
    db.commit()
    return redirect("/")

app.run(debug=True)
