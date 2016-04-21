import sys

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisabadkeybutitwilldo',
    ROOT_URLCONF=sys.modules[__name__],
)