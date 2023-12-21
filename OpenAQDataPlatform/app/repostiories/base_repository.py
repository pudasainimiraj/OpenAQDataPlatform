import abc
from sqlalchemy.orm import Session

class BaseRepository(abc.ABC):
    def __init__(self, session: Session):
        self.session = session

    def add(self, model):
        self.session.add(model)
        self.session.commit()

    def update(self, model, **kwargs):
        for key, value in kwargs.items():
            setattr(model, key, value)
        self.session.commit()

    def delete(self, model):
        self.session.delete(model)
        self.session.commit()

    def query_all(self):
        return self.session.query(self.model).all()

    def query_by_id(self, id):
        return self.session.query(self.model).filter_by(id=id).first()

    def query(self):
        return self.session.query(self.model)

    # Add more specific query methods as needed for each repository

    @abc.abstractmethod
    def get_or_create(self, **kwargs):
        pass

    @abc.abstractproperty
    def model(self):
        pass
