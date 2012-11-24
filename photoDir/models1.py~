from django.db import models
import datetime
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
    notes = models.TextField(required = False)
    office = models.CharField(max_length = 2, choices = OFFICE_CHOICES, required =
      False)
    postal_address = models.TextField(required = False)
    room = models.TextField(required = False)
    coordinates = GPSCoordinate(required = False)

class TextEmailField(models.EmailField):
    entity = models.ForeignKey(Entity)
    def get_internal_type(self):
        return u'TextField'

class TextPhoneField(models.TextField):
    number = TextField()
    description = TextField()
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

# This class is basically the "Person" class; however, it is called "Entity"
# to emphasize that it is intended to accommodate people, offices,
# organizational units, and possibly other areas.
class Entity(models.Model):
    active = models.BooleanField(required = False)
    department = models.ForeignKey(Entity, required = False)
    description = models.TextField(required = False)
    email = TextEmailField(required = False)
    extension = ExtensionField(required = False)
    homepage = TextURLField(required = False)
    image = models.FileField(required = False)
    location = LocationField(required = False)
    honorifics = models.TextField(required = False)
    name = models.TextField(required = False)
    post_nominals = models.TextField(required = False)    
    publish_externally = models.BooleanField(required = False)
    reports_to = models.ForeignKey(Entity, required = False)
    start_date = models.DateField(required = False)

# Tagging is intended at least initially to locate areas of expertise
# tagging.register(Entity)

