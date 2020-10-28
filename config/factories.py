from orator.orm import Factory
from app.User import User
from app.Car import Car
from app.Customer import Customer
from app.Engine import Engine
from app.ServiceHistory import ServiceHistory

factory = Factory()


def users_factory(faker):
    return {
        "name": faker.name(),
        "email": faker.email(),
        "password": "$2b$12$WMgb5Re1NqUr.uSRfQmPQeeGWudk/8/aNbVMpD1dR.Et83vfL8WAu",  # == 'secret'
    }


def customers_factory(faker):
    return {}


def cars_factory(faker):
    return {
        "make": faker.name(),
        "model": faker.company(),
        "year": faker.pyint(),
        "color": faker.safe_color_name(),
        "engine": faker.catch_phrase(),
        "mileage": faker.pyint(min_value=10, max_value=200000),
        "vin": faker.bban(),
        "msrp": faker.pyint()
    }


def engines_factory(faker):
    return {}


def service_history_factory(faker):
    return {}


factory.register(User, users_factory)
factory.register(Customer, customers_factory)
factory.register(Car, cars_factory)
factory.register(Engine, engines_factory)
factory.register(ServiceHistory, service_history_factory)
