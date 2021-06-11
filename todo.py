from flask import Flask, render_template, request
import datetime

from werkzeug.utils import redirect


app = Flask(__name__,template_folder="template")

lists = []

id=0

@app.route("/", methods=["GET","POST"])
def index():
    global id
    if request.method=="POST":
        task=request.form.get("task")
        time=request.form.get("time")
        if((task!=None) and (time!=None)):
            items={}
            items["task"]=task
            items["time"]=time
            items["id"]=id
            id=id+1
            lists.append(items)
        return render_template("index.html",lists=lists)
            
    else:
        return render_template("index.html",lists=lists)

@app.route("/delete/<int:key>")
def delete(key):
    for i in range(len(lists)):
        if (lists[i]["id"] == key):
            lists.pop(i)
            return redirect("/")
    return redirect("/")

@app.route("/updateform/<int:key>", methods=["GET","POST"])
def form(key):
        return render_template("index2.html",key=key) 

@app.route("/updateform/update/<int:key>", methods=["GET","POST"])
def update(key):
    newtask=request.form.get("newtask")
    for i in range(len(lists)):
        if (lists[i]["id"] == key):
            lists[i]["task"] == newtask
            return redirect("/")
    return redirect("/")        
        
    

app.run(debug=True)
