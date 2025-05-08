
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DateTime

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Event(Base):
    __tablename__ = "events"
    event_id: Mapped[str] = mapped_column(String, primary_key=True)
    type: Mapped[str] = mapped_column(String)
    user_id: Mapped[str] = mapped_column(String)
    repo: Mapped[str] = mapped_column(String)
    timestamp: Mapped[DateTime]
