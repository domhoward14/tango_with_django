import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PythonWorkSpace.settings')

import django
django.setup()

from rango.models import Category, Page

def add_page (cat,title,url, views = 0)
