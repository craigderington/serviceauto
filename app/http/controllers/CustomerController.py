"""A CustomerController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Customer import Customer


class CustomerController(Controller):
    """CustomerController Controller Class."""

    def __init__(self, request: Request):
        """CustomerController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        customers = Customer.all()
        return view.render("customers", {"customers": customers})
