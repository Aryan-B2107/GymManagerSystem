from backend.extensions import db


class ProgramType(db.Model):
    """Represents the types of fitness programs available."""
    __tablename__ = 'program_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    packages = db.relationship('MembershipPackage', backref='program_type', lazy=True)
