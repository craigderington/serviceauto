"""ServiceHistory Model."""

from config.database import Model


class ServiceHistory(Model):
    """ServiceHistory Model."""
    __fillable__ = ["service_date", "service_time", "service_rating", "car_id", 
                    "service_detail", "service_type"]
