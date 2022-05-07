from typing import Optional
from sqlmodel import SQLModel, Field, select
from datetime import datetime
from pydantic import validator
from statistics import mean


class Beer(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} informe o valor entre 1 até 10")
        return v

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


brewdog = Beer(name="Bewdog", style="NEIPA", flavor=6, image=8, cost=8)
