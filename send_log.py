#!/usr/bin/env python

from tspapi import API

api = API()


api.measurement_create(metric='CPU', value=0.8, source='log')

