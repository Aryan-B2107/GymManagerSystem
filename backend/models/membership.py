from backend.extensions import db
from datetime import datetime
from .member import Member # Import the Member model

class Membership(db.Model):
    """
    Represents a specific membership instance for a member.
    It now links to the MembershipPackage table.
    """
    __tablename__ = 'memberships'
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    membership_package_id = db.Column(db.Integer, db.ForeignKey('membership_packages.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=True)
    payments = db.relationship('Payment', backref='membership', lazy=True)