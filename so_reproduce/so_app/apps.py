from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SOAppConfig(AppConfig):
    name = "so_reproduce.so_app"
    verbose_name = _("SOApp")

    def ready(self):
        try:
            import so_reproduce.SOApp.signals  # noqa F401
        except ImportError:
            pass
