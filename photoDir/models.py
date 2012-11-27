from django.db import models
from datetime import datetime
import django.forms
import re

OFFICE_CHOICES = (
  (u'CN', u'Chicago North Office, Illinois, USA'),
  (u'CS', u'Chicago South Office, Illinois, USA'),
  (u'WH', u'Wheaton Office, Illinois, USA'),
  (u'SY', u'Sydney Office, New South Wales, Australia'),
  )


class ExtensionField(models.TextField):
    pass

#EXTENSION_LENGTH = 5

#def is_extension(number):
#    if len(str(number)) > EXTENSION_LENGTH:
#        raise forms.ValidationError(u'This extension is too long.')
#    #elif len(str(number)) < EXTENSION_LENGTH:
        #raise forms.ValidationError(u'This extension is too short.')
#    else:
#        return text
    
#class ExtensionField(PositiveIntegerField):
#    default_error_messages = {
#      u'invalid': u'Enter a valid extension.',
#      }
#    default_validators = [is_extension]

class Location(models.Model):
    notes = models.TextField(blank = True)
    office = models.CharField(max_length = 2, choices = OFFICE_CHOICES, blank = True)
    postal_address = models.TextField(blank = True)
    room = models.TextField(blank = True)
    #coordinates = GPSCoordinate(blank = True)

class TextPhoneField(models.TextField):
    number = models.TextField()
    description = models.TextField()
    def __eq__(self, other):
        try:
            return self.remove_formatting() == other.remove_formatting()
        except:
            return False
    def remove_formatting(self):
        return re.sub(ur'\D', u'', str(self))

class TextURLField(models.URLField):
    def get_internal_type(self):
        return u'TextField'


class TextEmailField(models.EmailField):
    entity = models.ForeignKey('Entity')
    def get_internal_type(self):
        return u'TextField'

# This class is basically the "Person" class; however, it is called "Entity"
# to emphasize that it is intended to accommodate people, offices,
# organizational units, and possibly other areas.
class Entity(models.Model):
    active = models.BooleanField(blank = True)
    department = models.ForeignKey('self', blank = True) 
    description = models.TextField(blank = True)
    email = TextEmailField()
    extension = ExtensionField(blank = True)
    homepage = TextURLField()
    image = models.FileField(upload_to='videos', max_length=100)
    #location = models.locationField(blank = True) locationfield is not defined.
    location = Location()
    honorifics = models.TextField(blank = True)
    name = models.TextField(blank = True)
    post_nominals = models.TextField(blank = True)    
    publish_externally = models.BooleanField(blank = True)
    #reports_to = models.ForeignKey('self', blank = True) only takes one self field
    start_date = models.DateField(blank = True)

# Tagging is intended at least initially to locate areas of expertise
# tagging.register(Entity)

class TextStatus(models.Model):
    datetime = models.DateTimeField(default=datetime.now)
    entity = models.ForeignKey(Entity)
    text = models.TextField()     

