#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Faraday Penetration Test IDE - Community Version
Copyright (C) 2013  Infobyte LLC (http://www.infobytesec.com/)
See the file 'doc/LICENSE' for the license information

'''
import logging
import logging.config
import os

logname = 'log.conf'

logpath = os.path.dirname(os.path.realpath(__file__))
logfile = os.path.join(logpath, logname)
logging.config.fileConfig(logfile)

def getLogger(obj=None):
    # create logger
    name = obj.__class__.__name__ if obj else 'Default'
    logger = logging.getLogger(name)
    return logger

