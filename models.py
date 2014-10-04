from run import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'rockets'

    id = db.Column(db.Integer, primary_key=True)
    var = db.Column(db.String())
    

    def __init__(self, var):
        self.var = var

    def __repr__(self):
        return '<id {}>'.format(self.id)
