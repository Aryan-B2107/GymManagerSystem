from backend.extensions import  db

class Permission(db.Model):
    """Represents a specific permission or capability in the system."""
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
