from . import db

class User(db.Model):
    __tablename__ = "users"   # 👈 add this line

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
 #   email = db.Column(db.String(100), nullable=False)  # 👈 include if your DB has email column

    def __repr__(self):
        return f"<User {self.name}>"

