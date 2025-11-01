from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class AnalyticsRecord(Base):
    __tablename__ = "analytics_records"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    metric_name: Mapped[str]
    metric_value: Mapped[float]
    collected_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

