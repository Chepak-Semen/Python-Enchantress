from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, text, JSON
from sqlalchemy.dialects.mysql import INTEGER


Base = declarative_base()
metadata = Base.metadata


class Student(Base):
    __tablename__ = 'students'

    id = Column(INTEGER(11), primary_key=True)
    enroll = Column(INTEGER(11))
    personal_info = Column(JSON)
    name = Column(String(255))
    created_on = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )
