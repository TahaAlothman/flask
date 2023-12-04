from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime





app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 
db=SQLAlchemy(app)
app.app_context().push()

class Message(db.Model):
    id =db.Column(db.Integer,primary_key=True) 
    user =db.Column(db.String(200),nullable=True)
    content =db.Column(db.String(500),nullable=True)
    created_at =db.Column(db.DateTime(),default =datetime.utcnow)


@app.route("/")
def hello():
    return "<h1>hello world<h1>"

if __name__ == "__main__":
    app.run(debug=True)  