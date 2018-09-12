from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@localhost/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)

@app.route('/')
def hello_world():
    return 'Hello World!'

def get_new_id():
    last_user = User.query.order_by(User.id).all()[-1]
    return last_user.id + 1

def create_user(name):
    new_id = get_new_id()
    new_user = User(id=new_id, name=name)
    db.session.add(new_user)
    db.session.commit()

def query_user(id):
    result = User.query.filter_by(id=id).first()
    print result.name

if __name__ == '__main__':
    # db.drop_all()
    print "hello"
    # db.create_all()
    create_user('xieen')
    # get_new_id()
    # query_user(1)
    app.run()