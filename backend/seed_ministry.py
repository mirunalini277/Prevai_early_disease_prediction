from backend.database import SessionLocal
from backend.models import User

def seed_ministry_user():
    db = SessionLocal()

    existing = db.query(User).filter(User.role == "ministry").first()
    if existing:
        print("Ministry user already exists")
        return

    user = User(
        email="ministry@health.gov",
        password="admin123",
        role="ministry"
    )

    db.add(user)
    db.commit()
    db.close()

    print("Ministry user created")

if __name__ == "__main__":
    seed_ministry_user()
