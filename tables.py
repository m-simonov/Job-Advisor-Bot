import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    tg_id = sa.Column(sa.Integer)
    username = sa.Column(sa.String, nullable=True)
    name = sa.Column(sa.String, nullable=True)

    def __repr__(self) -> str:
        return f"{self.username}"
