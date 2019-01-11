from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Movie(Base):
    __tablename__ = "movie"
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)


engine = create_engine('sqlite:////home/fox/Projects/Python_Playground/ORMs/example.db', echo=True)
# Base.metadata.create_all(bind=engine)
# sessionmaker allows us to make a session factory
Session = sessionmaker(bind=engine)


def select_user():
    session = Session()
    users = session.query(Movie).all()
    for user in users:
        print(user.username, user.id)


def add_new_user():
    session = Session()
    user = Movie()
    user.id = 0
    user.username = "alice"
    session.add(user)
    session.commit()
    session.close()


select_user()
