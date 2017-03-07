from app import db
from app.Model.UserModel import User
from datetime import datetime, timedelta
from sqlalchemy_utils import aggregated

#
# Relation Table for User, Study 
#
user_study_conn = db.Table('user_study_conn',
        db.Column('user_id',  db.Integer, db.ForeignKey('user.id')),
        db.Column('study_id', db.Integer, db.ForeignKey('study.id'))
)

class Study(db.Model) :
    """Study"""
    __tablename__ = 'study'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    
    created_date = db.Column(db.DateTime)

    users = db.relationship('User', secondary=user_study_conn, \
        backref=db.backref('studies', lazy='dynamic'))
    issues = db.relationship('StudyIssue', lazy='dynamic')
    events = db.relationship('Event', lazy='dynamic')

    @aggregated('users', db.Column(db.Integer))
    def user_num(self) :
        return db.func.count(User.id)

    def __init__(self, name, id=None, created_date=None) :
        self.name = name
        self.created_date = created_date or datetime.now()
        self.id = id

    def __repr__(self) :
        return '<Study {}, id: {}>'.format(self.name, self.id)

    def dict(self, join=False) :
        base = {
            'id': self.id,
            'name': self.name,
            'created_date': self.created_date,
        }
        if join :
            joined = {
                'users': [i.dict() for i in self.users],
                'issues': [i.dict() for i in self.issues]
            }
            base = dict(base, **joined)
        return base

class StudyIssue(db.Model) :
    __tablename__ = 'studyissue'
    id = db.Column(db.Integer, primary_key=True)
    study_id = db.Column(db.Integer, db.ForeignKey('study.id'))
    title = db.Column(db.Text)
    content = db.Column(db.Text)

    created_date = db.Column(db.DateTime)

    study = db.relationship('Study')

    def __init__(self, study_id, title='', content='', id=None, created_date=None) :
        self.title = title
        self.content = content
        self.study_id = study_id
        self.id = id
        self.created_date = created_date or datetime.now()
    def __repr__(self) :
        return '<StudyIssue id:{}, title:{}>'.format(self.id, self.title)
    def dict(self,join=False) :
        base = {
            'id':self.id,
            'title':self.title,
            'content':self.content
        }
        if join :
            joined = {
                'study':self.study.dict()
            }
            base = dict(base, **joined)
        return base