
from sqlalchemy import Integer, String, Text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, mapped_column
from contextlib import asynccontextmanager

Base = declarative_base()

class UserLetter(Base):
    __tablename__ = 'user_letter'

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(50))
    email = mapped_column(String(100))
    text = mapped_column(Text)
    delay = mapped_column(Integer)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

DATABASE_URL = "postgresql+asyncpg://postgres:1234@postgres:5432/mydata"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession)

@asynccontextmanager
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()