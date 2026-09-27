from sqlalchemy import TIMESTAMP, func
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from datetime import datetime
from app.config import settings


engine = create_async_engine(
    settings.database_url
)

async_session_maker = async_sessionmaker(
    engine,class_=AsyncSession, expire_on_commit=False
)

class Base(AsyncAttrs,DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,server_default=func.now(),onupdate=func.now()
    )