from sqlalchemy import Column, Integer, String, Text
from backend.database import Base

class HeroContent(Base):
    __tablename__ = "hero_content"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    subtitle = Column(Text)

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    body = Column(Text)
    image_path = Column(String(255), nullable=True)
