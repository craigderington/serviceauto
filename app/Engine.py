"""Engine Model."""

from config.database import Model


class Engine(Model):
    """Engine Model."""
    __fillable__ = ["horsepower", "liters", "serial_number", "mpg", "torque", 
                    "speed_rating"]
