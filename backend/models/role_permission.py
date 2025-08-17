from backend.extensions import db


class RolePermission(db.Model):
    """Links a user type to a permission."""
    __tablename__ = 'role_permissions'
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), primary_key=True)