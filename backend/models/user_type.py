from backend.extensions import db


class UserType(db.Model):
    """
        Defines the different user roles in the system.
        This is a lookup table to ensure data integrity for user roles.
        """
    __tablename__ = 'user_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # Relationship to the User model, where one UserType can have many Users
    users = db.relationship('User', backref='user_type', lazy=True)