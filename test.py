# -*- coding: utf-8 -*-
import datetime
import core

msg = core.crawl(datetime.datetime.now(), 1008)
#print msg
records = core.parser(msg)

