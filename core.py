# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
import urllib
import urllib2

def crawl(date, station):

    form = {
        "searchdate": str(date.year)+"/"+ str(date.month) +"/"+str(date.day),
        "fromstation":station #Taipei:1008
    }

    payload = urllib.urlencode(form)
   
    method = "http://twtraffic.tra.gov.tw/twrail/mobile/ie_stationsearchresult.aspx?"+ payload


    res = (urllib2.urlopen(method)).read()

    return res

def parser(data):
    regex   = ur"TRSearchResult\.push\(\'(.*?)\'*\)"
    records = re.findall(regex,data); 


    print "[INFO] Available ", len(records)

    tra_log = []
    #We group 6 cells into a record

    for idx in range(0, len(records), 6):
        
        try:
            tra = { 
                "type"  : records[idx],
                "number": records[idx+1],
                "time"  : records[idx+2],
                "to"    : records[idx+3],
                "dir"   : records[idx+4],
                "delay" : records[idx+5],
            }
        except:
            print "[ERROR] Index", idx

        tra_log.append(tra_log)
    
    return tra_log
