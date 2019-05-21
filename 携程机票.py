# encoding:utf-8
import requests
import jsonpath, json


class XCJP():
    def __init__(self):
        self.header = header = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "origin": "https://flights.ctrip.com",
            "referer": "https://flights.ctrip.com/itinerary/roundtrip/bjs-wuh?date=2019-06-04,2019-06-10"
        }

    def Get_City(self):
        get_url = "https://flights.ctrip.com/itinerary/api/poi/get"
        response = requests.get(get_url,headers=self.header)
        result = [m for k,v in json.loads(response.text)['data'].items() if isinstance(v,dict) for j,l in v.items() for m in l ]
        for info in result:
            cityname = info['display']
            city =  info['data'].split("|")[-1]
            cityid = info['data'].split("|")[-2]
            print(city,cityname,cityid)

    def Spider(self):
        post_url = "https://flights.ctrip.com/itinerary/api/12808/products"
        data = {"flightWay": "Roundtrip", "classType": "ALL", "hasChild": 'false', "hasBaby": 'false', "searchIndex": 1,
                "airportParams": [
                    {"dcity": "BJS", "acity": "WUH", "dcityname": "北京", "acityname": "武汉", "date": "2019-06-04",
                     "dcityid": 1, "acityid": 477},
                    {"dcity": "WUH", "acity": "BJS", "dcityname": "武汉", "acityname": "北京", "date": "2019-06-10",
                     "dcityid": 477, "acityid": 1}
                ]
                }
        response = requests.post(url=post_url, json=data, headers=self.header)
        for i in json.loads(response.text)['data']['routeList']:
            for j in i['legs']:
                print(j['flight'])


if __name__ == '__main__':
    x = XCJP()
    x.Spider()
    # x.Get_City()
