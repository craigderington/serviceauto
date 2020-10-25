from orator.migrations import Migration


class Car(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("cars") as table:
            table.increments("id")
            table.text("make")
            table.text("model")
            table.integer("year")
            table.integer("mileage")
            table.text("vin")
            table.text("engine")
            table.integer("msrp")
            table.text("color")
            table.timestamps()
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")

    def down(self):
        """
        Revert the migrations.
        """
        pass
