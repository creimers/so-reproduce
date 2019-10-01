from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "so_reproduce.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import so_reproduce.users.signals  # noqa F401
        except ImportError:
            pass
