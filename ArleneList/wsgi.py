

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('path/to/yourprojectenv/lib/python3.8/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ArleneList.settings')

application = get_wsgi_application()
