# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:

import os
import sys

# Assuming your django settings file is at:
# '/home/Tamanna12/sangamuniversity/sangamuniversity/settings.py'
# And your manage.py is at '/home/Tamanna12/sangamuniversity/manage.py'

path = '/home/Tamanna12/sangamuniversity'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'sangamuniversity.settings'

# Then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
