"""Car Model."""

from config.database import Model
from orator.orm import belongs_to


class Car(Model):
    """Car Model."""
    __fillable__ = ["make", "model", "year", "engine", "mileage", "vin",
                    "color", "msrp", "options"]

    @belongs_to("user_id", "id")
    def user(self):
        from app.User import User
        return User
