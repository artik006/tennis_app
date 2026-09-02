from backend.database import Base, engine
from backend.models.content import HeroContent, News

Base.metadata.create_all(bind=engine)
