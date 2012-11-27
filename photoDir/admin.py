import django.contrib.admin
import photoDir.models
#import tagging

django.contrib.admin.autodiscover()
django.contrib.admin.site.register(photoDir.models.Entity)
django.contrib.admin.site.register(photoDir.models.Location)
#tagging.register(directory.models.Entity)
