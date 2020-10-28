from orator.seeds import Seeder
from app.Car import Car
from config.factories import factory


class CarTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        factory(Car, 50).create()
