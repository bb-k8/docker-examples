from flask_app.models import db


class User(db.Model):  # pylint: disable=too-few-public-methods
    """
    Cluster Agent Server model class for db operations
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)  # pylint: disable=invalid-name
    user_id = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    def __str__(self):
        return f"User(user_id={self.user_id}, first_name={self.first_name}, last_name={self.last_name})"

class UserOperations:
    @staticmethod
    def get_all(db_session, **filters):
        return db_session.query(User).filter_by(**filters).all()
    @staticmethod
    def create_user(db_session, **params):
        new_user = User(**params)
        db_session.add(new_user)
