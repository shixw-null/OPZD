from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get(self, id):
        return self.session.query(self.model).filter(self.model.id == id).first()

    def find(self, **kwargs):
        return self.session.query(self.model).filter_by(**kwargs).all()

    def get_all(self):
        return self.session.query(self.model).all()

    def save(self, entity):
        self.session.add(entity)
        self.session.commit()

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()