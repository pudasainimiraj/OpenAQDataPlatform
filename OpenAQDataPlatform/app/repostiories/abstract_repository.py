import abc
from sqlalchemy.orm import Session

"""_summary_

    Returns:
        _type_: _description_
    """
class BaseRepository(abc.ABC):
    def __init__(self, session: Session):
        self.session = session
    def add(self, model):
        self.session.add(model)
        self.session.commit()

    def add_all(self, models):
        self.session.add_all(models)
        self.session.commit()

    def delete(self, model):
        self.session.delete(model)
        self.session.commit()

    def delete_all(self, models):
        for model in models:
            self.session.delete(model)
        self.session.commit()

    def query(self, model):
        return self.session.query(model)

    def query_all(self, model):
        return self.session.query(model).all()

    def query_by_id(self, model, id):
        return self.session.query(model).filter_by(id=id).first()

    def query_by_name(self, model, name):
        return self.session.query(model).filter_by(name=name).first()

    def query_by_name_and_id(self, model, name, id):
        return (
            self.session.query(model)
            .filter_by(name=name)
            .filter_by(id=id)
            .first()
        )

    def query_by_name_and_id_or_create(
        self, model, name, id, **kwargs
    ):
        return (
            self.session.query(model)
            .filter_by(name=name)
            .filter_by(id=id)
            .first()
            or model(name=name, id=id, **kwargs)
        )

    def query_by_name_or_create(self, model, name, **kwargs):
        return (
            self.session.query(model)
            .filter_by(name=name)
            .first()
            or model(name=name, **kwargs)
        )

    def query_by_name_and_id_or_create_with_session(
        self, model, name, id, **kwargs
    ):
        return (
            self.session.query(model)
            .filter_by(name=name)
            .filter_by(id=id)
            .first()
            or model(name=name, id=id, **kwargs)
        )
