from backend.extensions import db


class MembershipPlan(db.Model):
    """
    Defines the available membership plans offered by the
    """
    __tablename__ = 'membership_plans'
    id = db.Column(db.Integer, primary_key=True)
    program_type = db.Column(db.String(50), unique=True, nullable=False)
    membership_length_months = db.Column(db.Integer, nullable=False)
    fees = db.Column(db.Numeric(10, 2), nullable=False)
