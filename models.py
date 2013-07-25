from django.db import models
from django.core.cache import cache
from django.conf import settings
from jmbo.models import ModelBase
from wunderground.constants import *
from wunderground.api import Wunderground, WundergroundException

class Feed(models.Model):

    location = models.CharField(
        max_length=255, 
        unique=True,
        help_text="A location, eg. Pretoria or Johannesburg"
    )
    
    country_code = models.CharField(
       'Country Code',
       max_length=10,
       choices=WUNDERGROUND_ISO_CHOICES,
       default=WUNDERGROUND_DEFAULT_COUNTRY
    )
    
    default = models.BooleanField(
      help_text="Set this location as the default"
    )