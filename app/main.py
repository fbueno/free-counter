#!/usr/bin/env python
# coding: utf-8

import logging
from time import time

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import memcache

import views

# uri mapping - pascal triangle.
urls = (
  (r'/get/', views.Get),
)

def real_main():
  app = webapp.WSGIApplication(urls, debug=False)
  util.run_wsgi_app(app)

def profile_main():
    start=time()
    real_main()
    memcache.set('time', time() - start)

main=profile_main

if __name__ == '__main__':
  log = logging.getLogger()
  log.setLevel(logging.ERROR)
  main()
