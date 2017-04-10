# -*- coding: utf-8 -*-

from app import db
from app.Model.StudyModel import Study, StudyIssue

DEFAULT_PAGE_SIZE = 20

def get(id) :
    return db.session.query(Study).get(id)

def getAll() :
    return db.session.query(Study).all()

def getPage(page, owner_id=None, **kwargs) :
    q = db.session.query(Study)
    pageSize = args.get('pageSize') or DEFAULT_PAGE_SIZE
    if owner_id != None :
        q = q.filter(Study.owner_id == int(owner_id))
    return q.limit(pageSize).offset(page*pageSize).all()

def create(owner_id, **args) :
    obj = Study(owner_id=owner_id, **args)
    db.session.add(obj)
    db.session.commit()
    return obj

def delete(obj) :
    db.session.delete(obj)
    db.session.commit()

def checkName(name) :
    return True if db.session.query(Study).filter(Study.name == name).first() else False

def getIssue(id) :
    return db.session.query(StudyIssue).get(id)

def createIssue(**args) :
    obj = StudyIssue(**args)
    db.session.add(obj)
    db.session.commit()
    return obj
