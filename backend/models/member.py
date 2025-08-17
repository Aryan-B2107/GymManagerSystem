from backend.extensions import db # Use the same import path as membership.py

class Member(db.Model):
    """
    This table stores the personal information for a gym member.
    It has a one-to-one relationship with the User table for login.
    """
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    full_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    locality = db.Column(db.String(100))
    memberships = db.relationship('Membership', backref='member', lazy=True)
    user = db.relationship('User', backref='member_profile', uselist=False)