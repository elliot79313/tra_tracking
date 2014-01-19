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
        "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,fil;q=0.2",
        "Accept-Encoding":"gzip,deflate,sdch",
        'Accept-Charset': 'utf-8',
        "Connection":"keep-alive",
        "Cookie":"ASP.NET_SessionId=pg3rikrhdmxshv55zbhw2k45",
        "Cache-Control":"max-age=0",
        "Host":"twtraffic.tra.gov.tw",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
    }
    print method
    req = urllib2.Request(method, headers=headers)
    res = (urllib2.urlopen(req)).read()

    print res
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
   
