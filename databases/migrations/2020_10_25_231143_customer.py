from orator.migrations import Migration


class Customer(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("customers") as table:
            table.increments("id")
            table.text("first_name")
            table.text("last_name")
            table.text("email")
            table.text("phone")
            table.integer("serviceaddress_id").unsigned()
            table.foreign("serviceaddress_id").references("id").on("serviceaddresses")
            table.text("verified")
            table.text("salesagent")
            table.text("marketing")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        pass
