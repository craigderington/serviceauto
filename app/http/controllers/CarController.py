"""A CarController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Car import Car


class CarController(Controller):
    """CarController Controller Class."""

    def __init__(self, request: Request):
        """CarController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        cars = Car.all()
        return view.render("cars.html", {"cars": cars})

    def single(self, view: View, request: Request):
        param = self.request.id
        car = Car.find(param)
        return view.render(
            "car.html",
            {"car": car}
        )
