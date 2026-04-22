from app.database import SessionLocal, Base, engine
from app.models import Role, Permission, User
from app.auth import hash_password

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Check if already seeded
existing = db.query(User).filter(User.email == "admin@assetvault.com").first()

if existing:
    print("⚠️ Already seeded")
else:
    p1 = Permission(name="delete:asset")
    p2 = Permission(name="view:inventory")

    admin_role = Role(name="Admin", permissions=[p1, p2])
    emp_role = Role(name="Employee", permissions=[])

    admin = User(
        email="admin@assetvault.com",
        hashed_password=hash_password("admin123"),
        role=admin_role
    )

    emp = User(
        email="employee@assetvault.com",
        hashed_password=hash_password("emp123"),
        role=emp_role
    )

    db.add_all([p1, p2, admin_role, emp_role, admin, emp])
    db.commit()

    print("✅ Seed done")

db.close()