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

    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip,deflate,sdch",
        'Accept-Charset': 'utf-8',
    }
    print method
    req = urllib2.Request(method, headers=headers)

    res = (urllib2.urlopen(req)).read()

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
                "type"  : record[idx],
                "number": record[idx+1],
                "time"  : record[idx+2],
                "to"    : record[idx+3],
                "dir"   : record[idx+4],
                "delay" : record[idx+5],
            }
        except:
            print "[ERROR] Index", idx

        tra_log.append(tra_log)

    return tra_log
   
