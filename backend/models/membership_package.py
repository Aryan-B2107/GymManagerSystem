from backend.extensions import db


class MembershipPackage(db.Model):
    """
    This defines a specific package offered by the gym, linking a program
    type to a duration and a fee.
    """
    __tablename__ = 'membership_packages'
    id = db.Column(db.Integer, primary_key=True)
    # This foreign key links to the ProgramType table
    program_type_id = db.Column(db.Integer, db.ForeignKey('program_types.id'), nullable=False)
    duration_months = db.Column(db.Integer, nullable=False)
    fees = db.Column(db.Numeric(10, 2), nullable=False)

    # Relationships
    program_type = db.relationship('ProgramType', backref='packages', lazy=True)
    memberships = db.relationship('Membership', backref='membership_package', lazy=True)