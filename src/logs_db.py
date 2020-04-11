from sqlalchemy import Column, String

from src.db_entity import Entity, Base



class Logs(Entity, Base):
    __tablename__ = 'logs'

    httpmethod = Column(String)
    requestpath = Column(String)
    status = Column(String)
    timetook = Column(String)

    def __init__(self, httpmethod, requestpath, status, timetook, created_by):
        Entity.__init__(self, created_by)
        self.httpmethod = httpmethod
        self.requestpath = requestpath
        self.status = status
        self.timetook = timetook