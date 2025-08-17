from backend.extensions import db
class User(db.Model):
    """Represents a user account for login and access control."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'), nullable=False)
    member = db.relationship('Member', backref='user', lazy=True, uselist=False)
