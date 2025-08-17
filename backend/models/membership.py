from backend.extensions import db
from datetime import datetime

class Membership(db.Model):
    """
    Represents an instance of a member's subscription to a plan.
    This is the key join table that links a member to a plan.
    """
    __tablename__ = 'memberships'
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    membership_plan_id = db.Column(db.Integer, db.ForeignKey('membership_plans.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=True)

    # Relationship to the Payment table (one Membership can have many Payments)
    payments = db.relationship('Payment', backref='membership', lazy=True)
