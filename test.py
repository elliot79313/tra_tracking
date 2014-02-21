# -*- coding: utf-8 -*-
import datetime
import core
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

fetchDate = datetime.datetime.now()
msg = core.crawl(fetchDate, 1008)
#print msg
records = core.parser(fetchDate, msg)

