"""A ServiceAddressController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.ServiceAddress import ServiceAddress


class ServiceAddressController(Controller):
    """ServiceAddressController Controller Class."""

    def __init__(self, request: Request):
        """ServiceAddressController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        sa = ServiceAddress.all()
        return view.render("serviceaddresses", {"addresses": sa})
