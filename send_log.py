#!/usr/bin/env python

from datetime import datetime
from tspapi import API
from tspapi import Measurement
from random import randrange
from logme import LogMe
from time import sleep


class SendLog(object):

    def __init__(self):
        self.api = API()
        self.log = LogMe()

    def send_measurements(self):
        while True:
            m = Measurement(metric='CPU', value=randrange(0,100)/100.0,
                            source='foo', timestamp=datetime.now())
            self.api.measurement_create_batch([m])
            self.log.log(metric=m.metric, value=m.value, source=m.source, timestamp=m.timestamp)
            sleep(5)


def execute():
    s = SendLog()
    s.send_measurements()



