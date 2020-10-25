"""User Model."""

from config.database import Model
from orator.orm import has_many


class User(Model):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __auth__ = "email"

    @has_many("id", "user_id")
    def cars(self):
        from app.Car import Car
        return Car
