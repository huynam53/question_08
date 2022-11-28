class AuthRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to a replica.
        """
        return 'slave'

    def db_for_write(self, model, **hints):
        """
        Writes always go to master ie default.
        """
        return 'master'
