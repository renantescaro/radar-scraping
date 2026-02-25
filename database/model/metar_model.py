from sqlmodel import Field, SQLModel, UniqueConstraint
from typing import Optional


class Metar(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("icao", "date_time", name="unique_icao_datetime"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    icao: str = Field(index=True)
    date_time: str = Field(index=True)

    latitude: Optional[str] = Field(default=None)
    longitude: Optional[str] = Field(default=None)
    elevation_m: Optional[str] = Field(default=None)
    ceiling_is_minimum: Optional[str] = Field(default=None)
    visibility_is_minimum: Optional[str] = Field(default=None)
    temperature: Optional[str] = Field(default=None)
    dew_point: Optional[str] = Field(default=None)
    relative_humidity: Optional[str] = Field(default=None)
    wind_direction: Optional[str] = Field(default=None)
    wind_speed: Optional[str] = Field(default=None)
    wind_gust_mps: Optional[str] = Field(default=None)
    visibility: Optional[str] = Field(default=None)
    extinction_per_km: Optional[str] = Field(default=None)
    msl_pres: Optional[str] = Field(default=None)
    city_name: Optional[str] = Field(default=None)
