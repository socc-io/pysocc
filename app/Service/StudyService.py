from app import db
from app.Model.StudyModel import Study

def get(id) :
    return db.session.query(Study).get(id)

def create(**args) :
    obj = Study(**args)
    db.session.add(obj)
    db.session.commit()
    return obj

def delete(obj) :
    db.session.delete(obj)
    db.session.commit()

def deleteById(id) :
    obj = get(id)
    if obj:
        delete(obj)
        return True
    return False
