# -*- coding: utf-8 -*-
import datetime
import core
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

msg = core.crawl(datetime.datetime.now(), 1008)
#print msg
records = core.parser(msg)

