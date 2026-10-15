from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Boolean,Date
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class todo(db.Model):
    id=db.Column(Integer,primary_key=True)
    title=db.Column(String(100),nullable=False)
    description=db.Column(String(500))
    priority=db.Column(String,nullable=False)
    is_complete=db.Column(Boolean,default=False)
    due_date=db.Column(Date,nullable=False)


@app.route("/")
def home():
    return render_template("index.html",todo=todo)
@app.route('/submit',methods=["POST"])
def submit():
    title=request.form.get("title")
    description=request.form.get("description")
    priority=request.form.get("priority")
    is_complete=request.form.get("is_completed") == "on"
    due_date=request.form.get("due_date")
    due_date=datetime.strptime(due_date,'%Y-%m-%d')

    t1=todo(title=title,description=description,priority=priority,is_complete=is_complete,due_date=due_date)

    db.session.add(t1)    
    db.session.commit()
    return render_template("index.html",message="Task Add Successfully")

@app.route('/get',methods=['GET'])
def show():
    t1=todo.query.all()
    print(t1)
    return render_template("index.html",t1=t1)
@app.route("/delete", methods=['POST'])
def delete_todo():
    d_id = request.form.get("d_id")
    print(d_id)
    
    t1 = todo.query.get(d_id)
    
    db.session.delete(t1)
    db.session.commit()
    
    return redirect("/get")
if __name__=="__main__":
    with app.app_context():
      db.create_all()
    app.run(debug=True)

from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Boolean,Date
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class todo(db.Model):
    id=db.Column(Integer,primary_key=True)
    title=db.Column(String(100),nullable=False)
    description=db.Column(String(500))
    priority=db.Column(String,nullable=False)
    is_complete=db.Column(Boolean,default=False)
    due_date=db.Column(Date,nullable=False)


@app.route("/")
def home():
    return render_template("index.html",todo=todo)
@app.route('/submit',methods=["POST"])
def submit():
    title=request.form.get("title")
    description=request.form.get("description")
    priority=request.form.get("priority")
    is_complete=request.form.get("is_completed") == "on"
    due_date=request.form.get("due_date")
    due_date=datetime.strptime(due_date,'%Y-%m-%d')

    t1=todo(title=title,description=description,priority=priority,is_complete=is_complete,due_date=due_date)

    db.session.add(t1)    
    db.session.commit()
    return render_template("index.html",message="Task Add Successfully")

@app.route('/get',methods=['GET'])
def show():
    t1=todo.query.all()
    print(t1)
    return render_template("index.html",t1=t1)
@app.route("/delete", methods=['POST'])
def delete_todo():
    d_id = request.form.get("d_id")
    print(d_id)
    
    t1 = todo.query.get(d_id)
    
    db.session.delete(t1)
    db.session.commit()
    
    return redirect("/get")
if __name__=="__main__":
    with app.app_context():
      db.create_all()
    app.run(debug=True)

