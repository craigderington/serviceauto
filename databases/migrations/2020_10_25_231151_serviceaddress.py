from orator.migrations import Migration


class Serviceaddress(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("serviceaddresses") as table:
            table.increments("id")
            table.integer("street_number")
            table.text("street_name")
            table.text("street_other")
            table.text("city")
            table.text("state")
            table.text("zipcode")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        pass
