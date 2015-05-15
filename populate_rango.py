import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PythonWorkSpace.settings')

import django
django.setup()

from rango.models import Category, Page

def add_page (cat,title,url, views = 0):
    Page.objects.get_or_create(category=cat, title = title, url= url, views = views)


def add_cat(name):
    c = Category.objects.get_or_create(name = name)[0]
    return c

def populate():
    python_cat = add_cat('Python')

    add_page(cat = python_cat,
             title = "Official Python Tutorial",
             url = "http://docs.python.org/2/tutorial/")

    add_page(python_cat,
             "Learn Python in 10 minutes",
             "http//:www.korokithakis.net/tutorials/python")

    add_page(cat = python_cat,
             title = "How to Think like a Computer Scientist",
             url = "http://www.korokithakis.net/tutorials/python")

    django_cat = add_cat(name = "Django")

    add_page(cat = django_cat,
             title = "Official Django Tutorial",
             url = "https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat = django_cat,
             title = "Django Rocks",
             url = "http://www.djangorocks.com/")

    add_page(cat = django_cat,
             title = "How to Tango with Django",
             url = "http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks")

    add_page(frame_cat,
             "Bottle",
             "http://bottlepy.org/docs/dev")

    add_page(frame_cat,
             "Flask",
             "http://flask.pocoo.org")

    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print "- {0} - {1}".format(str(c), str(p))


if __name__ == '__main__':
    print "starting Rango population script"
    populate()