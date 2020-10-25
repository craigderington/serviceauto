from orator.migrations import Migration


class Servicehistory(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("servicehistories") as table:
            table.increments("id")
            table.datetime("service_date")
            table.datetime("service_time")
            table.integer("car_id").unsigned()
            table.foreign("car_id").references("id").on("cars")
            table.text("service_detail")
            table.text("service_type")
            table.integer("service_rating")

    def down(self):
        """
        Revert the migrations.
        """
        pass
