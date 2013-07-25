from django.conf import settings
from django.core.cache import cache
from jmbo_weather.models import *
from jmbo_weather.constants import *

import datetime
import json
import logging
import urllib2

logger = logging.getLogger('django')

class WundergroundException(Exception):
    pass

class Wunderground(object):

    # Weather Underground Response format JSON/XML
    RESPONSE_FORMAT = 'json'
    
    # Weather underground base url %s will be replaced by the api key
    BASE_URL = 'http://api.wunderground.com/api/%s'  
    
    # Feed cache time
    CACHE_TIMEOUT = 300    
    
    ''' 
    Weather Underground Service Urls
    As defined @ http://www.wunderground.com/weather/api/d/docs
    '''   
    SERVICE_ALERTS = 'alerts'
    SERVICE_ALMANAC = 'almanac'
    SERVICE_ASTRONOMY = 'astronomy'
    SERVICE_CONDITIONS = 'conditions'
    SERVICE_CURRENTHURRICANE = 'currenthurricane'
    SERVICE_FORECAST = 'forecast'
    SERVICE_FORECAST10DAY = 'forecast10day'
    SERVICE_GEOLOOKUP = 'geolookup'
    SERVICE_HISTORY = 'history'
    SERVICE_HOURLY = 'hourly'
    SERVICE_HOURLY10DAY = 'hourly10day'
    SERVICE_PLANNER = 'planner'
    SERVICE_RAWTIDE = 'rawtide'
    SERVICE_SATELLITE = 'satellite'
    SERVICE_TIDE = 'tide'
    SERVICE_WEBCAMS = 'webcams'
    SERVICE_YESTERDAY = 'yesterday'
    
    def __init__(self):
        self.api_key    = getattr(settings,'WUNDERGROUND_API_KEY', '')
        
        if self.RESPONSE_FORMAT == 'xml':
            raise WunderGroundException("XML Response format not currently supported")

    def _get_weather(self, url):
        # Set API Key into url
        url = self.BASE_URL % (self.api_key,) + url
        logger.debug(url)
        try:
            f = urllib2.urlopen(url)
            response = f.read()
            f.close() 
            if self.RESPONSE_FORMAT == 'json':
                return json.loads(json_string)
            else:
                # TODO: build in xml functionality
                return response
        except urllib2.URLError, e:
            if settings.DEBUG:
                raise e
            else:
                # Error fetching url, either net issue or feed does not exist
                logger.error(
                    'jmbo_weather.api._get_weather: ' + e.reason
                )
                return None

    def _cache_key(self, *args):
        return 'wunderground_feed_%s' % ('_'.join(str(value).replace(" ", "_") for value in args))

    def _request(self, service, code, location):
        cache_key = self._cache_key(service, code, location)
        cached = cache.get(cache_key, None)
        if (cached is not None) and not force:
            return cached        
        else:
            feed = self._get_weather('/%s/q/%s/%s.%s' % (service, str(code), str(location).replace(" ", "_"), self.RESPONSE_FORMAT))
            cache.set(cache_key, feed, self.CACHE_TIMEOUT)
            return feed

    def _request_date(self, service, date, code, location):
        cache_key = self._cache_key(service, date, code, location)
        cached = cache.get(cache_key, None)
        if (cached is not None) and not force:
            return cached        
        else:
            feed = self._get_weather('/%s_%s/q/%s/%s.%s' % (service, str(date), str(code), str(location).replace(" ", "_"), self.RESPONSE_FORMAT))
            cache.set(cache_key, feed, self.CACHE_TIMEOUT)
            return feed

    def alerts(self, code, location):
        return self._request(self.SERVICE_ALERTS, code, location)

    def almanac(self, code, location):
        return self._request(self.SERVICE_ALMANAC, code, location)

    def astronomy(self, code, location):
        return self._request(self.SERVICE_ASTRONOMY, code, location)

    def conditions(self, code, location):
        return self._request(self.SERVICE_CONDITIONS, code, location)
        
    def currenthurricane(self, code, location):
        return self._request(self.SERVICE_CURRENTHURRICANE, code, location)

    def forecast(self, code, location):
        return self._request(self.SERVICE_FORECAST, code, location)
        
    def forecast10day(self, code, location):
        return self._request(self.SERVICE_FORECAST10DAY, code, location)
        
    def geolookup(self, date, code, location):
        return self._request(self.SERVICE_GEOLOOKUP, code, location)
        
    def history(self, date, code, location):
        return self._request_date(self.SERVICE_HISTORY, date, code, location)
        
    def hourly(self, code, location):
        return self._request(self.SERVICE_HOURLY, code, location)
        
    def hourly10day(self, code, location):
        return self._request(self.SERVICE_HOURLY10DAY, code, location)
        
    def planner(self, date, code, location):
        return self._request_date(self.SERVICE_PLANNER, date, code, location)
        
    def rawtide(self, code, location):
        return self._request(self.SERVICE_RAWTIDE, code, location)

    def satellite(self, code, location):
        return self._request(self.SERVICE_SATELLITE, code, location)
        
    def tide(self, code, location):
        return self._request(self.SERVICE_TIDE, code, location)
        
    def webcams(self, code, location):
        return self._request(self.SERVICE_WEBCAMS, code, location)
        
    def yesterday(self, code, location):
        return self._request(self.SERVICE_YESTERDAY, code, location)
        
                                                                                                                    