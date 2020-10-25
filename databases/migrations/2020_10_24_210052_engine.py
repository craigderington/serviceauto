from orator.migrations import Migration


class Engine(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("engines") as table:
            table.increments("id")
            table.integer("horsepower")
            table.integer("liters")
            table.text("serial_number")
            table.integer("mpg")
            table.text("speed_rating")
            table.integer("torque")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        pass
