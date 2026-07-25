import os

from sqlalchemy.orm import Session

from app.config.database import SessionLocal
from app.models.user import User, UserStatus
from app.services.auth_services import AuthServices


def seed_admin(db: Session = None):
    session = db or SessionLocal()
    try:
        admin_username = os.getenv("ADMIN_USER", "admin")
        admin_password = os.getenv("ADMIN_PASSWORD", "password")

        # Check if the admin user already exists
        admin = session.query(User).filter(User.user_name == admin_username).first()
        if not admin:
            hashed_pwd = AuthServices.hash_password(admin_password)
            admin_user = User(
                user_name=admin_username,
                hashed_password=hashed_pwd,
                full_name="System Administrator",
                nick_name="Admin",
                contact_info="admin@firstdrink.com",
                address="Dev HQ",
                status=UserStatus.IN_PARTY,
                is_admin=True,
            )
            session.add(admin_user)
            session.commit()
            print(f"Admin user '{admin_username}' seeded successfully!")
        else:
            print(f"Admin user '{admin_username}' already exists.")
    except Exception as e:
        session.rollback()
        print(f"❌ Seeding failed: {e}")
        raise e
    finally:
        if not db:
            session.close()


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    seed_admin()
