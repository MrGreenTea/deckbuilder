from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = "mtg_deckbuilder.users"
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        try:
            # TODO
            import users.signals  # pylint: disable=unused-variable
        except ImportError:
            pass
