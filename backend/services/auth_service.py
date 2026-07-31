import re
import bcrypt

from backend.models import User


class AuthService:

    @staticmethod
    def register_user(db, full_name, email, password):

        full_name = full_name.strip()
        email = email.strip().lower()

        if not full_name:
            return False, "Full name is required."

        if not email:
            return False, "Email is required."

        email_pattern = r"^(?!.*\.\.)[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+$"

        if not re.fullmatch(email_pattern, email):
            return False, "Please enter a valid email address."

        if len(password) < 8:
            return False, (
                "Password must be at least 8 characters long and include "
                "an uppercase letter, a lowercase letter, a number, and a special character."
            )

        if not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter."

        if not re.search(r"[a-z]", password):
            return False, "Password must contain at least one lowercase letter."

        if not re.search(r"\d", password):
            return False, "Password must contain at least one number."

        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
            return False, "Password must contain at least one special character."

        existing_user = db.query(User).filter(User.email == email).first()

        if existing_user:
            return False, "Email already registered."

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password
        )

        db.add(new_user)
        db.commit()

        return True, "Registration successful."

    @staticmethod
    def login_user(db, email, password):

        email = email.strip().lower()

        user = db.query(User).filter(User.email == email).first()

        if not user:
            return None

        if bcrypt.checkpw(
            password.encode("utf-8"),
            user.password.encode("utf-8")
        ):
            return user

        return None