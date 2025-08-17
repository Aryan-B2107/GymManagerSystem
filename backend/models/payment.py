from backend.extensions import db
from datetime import datetime
class Payment(db.Model):
    """
    Represents a payment record for a membership.
    The `package_cost` field has been added to match the updated database schema.
    """
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    membership_id = db.Column(db.Integer, db.ForeignKey('memberships.id'), nullable=False)
    package_cost = db.Column(db.Float, nullable=False)
    amount_paid = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
