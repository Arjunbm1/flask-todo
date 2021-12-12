from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import selectin_polymorphic
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


def __init__(self, sno, title, desc, date_created):
    self.sno = sno
    self.title = title
    self.desc = desc
    self.date_created = date_created

@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    alltodo = Todo.query.all()
    return render_template("index2.html", alltodo=alltodo)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>",  methods=['GET','POST'])
def update(sno):
  if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo= Todo.query.filter_by(sno=sno).first()
        todo.title= title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

  todo = Todo.query.filter_by(sno=sno).first()
  return render_template('update.html', todo=todo)

if __name__ == "main":
    app.run(debug=True, host="0.0.0.0")
