from main import db

class Msg(db.Model):
    '''set structure of database'''
    sno = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50),  nullable=False)
    # phone_num = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(200),  nullable=False)
    date = db.Column(db.String(20),  nullable=True)

class Posts(db.Model):
    '''set structure of posts database'''
    sno = db.Column(db.Integer, primary_key=True,)
    title = db.Column(db.String(80), nullable=False)
    # tagline = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(35),  nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(12),  nullable=False)
    img_file = db.Column(db.String(20),  nullable=True)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))