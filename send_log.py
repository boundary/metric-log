#!/usr/bin/env python

from datetime import datetime
from tspapi import API
from tspapi import Measurement
from random import randrange
from logme import LogMe
from time import sleep

api = API()
log = LogMe()

while True:
    m = Measurement(metric='CPU', value=randrange(0,100)/100.0, source='foo', timestamp=datetime.now())
    api.measurement_create_batch([m])
#    log.log(metric=m.metric, value=m.value, source=m.source, timestamp=m.timestamp)
    sleep(5)


