from backend.database import engine
from backend.models import Base


def create_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database created successfully.")


if __name__ == "__main__":
    create_database()