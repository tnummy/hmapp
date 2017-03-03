
import requests
import xmltodict
from flask import jsonify
from lxml import html
from collections import defaultdict



print 'Prop120'.split('Prop')


response = requests.get('https://ws-playground.luceosolutions.com/rest/doc/requisitions', auth=('playground', 'PZWcKUPyn'))
page = html.fromstring(response.content)
propID = page.xpath('/html/body/div/div[2]/table/tbody/tr/td[1]/text()')
propMeaning = page.xpath('/html/body/div/div[2]/table/tbody/tr/td[2]/text()')
propType = page.xpath('/html/body/div/div[2]/table/tbody/tr/td[3]/text()')
propValue = page.xpath('/html/body/div/div[2]/table/tbody/tr/td[4]/a')

props = page.xpath('/html/body/div/div[2]/table/tbody/tr')

# # print props #.xpath('//td[1]/text()')
flatten = lambda l: [item for sublist in l for item in sublist]
propDict = []
for p in props:
    req_field_type = p.xpath('./td[3]/text()')
    print req_field_type
    url = p.xpath('./td[4]/a/text()')
    if req_field_type == 'Integer':
        field_type = ['number']
    elif len(url) > 0:
        field_type = ['select']
    elif req_field_type == 'Date':
        field_type = ['date']
    else:
        field_type = ['text']


    propDict.append(flatten([p.xpath('./td[1]/text()'), p.xpath('./td[2]/text()'), field_type, url]))

# print propDict
    # print [p.xpath('./td[1]/text()'), p.xpath('./td[2]/text()'), p.xpath('./td[3]/text()'), p.xpath('./td[4]/a/text()')]
# print propDict[3][3]
# response = xmltodict.parse(requests.get(propDict[3][3], auth=('playground', 'PZWcKUPyn')).text)['root']['result']
# for key, value in response.items():
#     for piece in value:
#         print {'id': piece['id'], 'label': piece['lib']}
# for p in propDict:
#     if len(p) == 4:
#         url = p.pop(3)
#         response = xmltodict.parse(requests.get(url, auth=('playground', 'PZWcKUPyn')).text)['root']['result']
#         # p.append(response)
#         for k, v in response.items():
#             for s in v.items():
#                 print s


for p in propDict:
    if len(p) == 4:
        url = p.pop(3)
        response = xmltodict.parse(requests.get(url, auth=('playground', 'PZWcKUPyn')).text)['root']
        # print response['recordCount']
        if int(response['recordCount']) > 1:
            plist = []
            for key, value in response['result'].items():
                for piece in value:
                # print key, value
                    plist.append({'id': piece['id'], 'lib': piece['lib']})
            p.append(plist)
        else:
            p.append([{'id': response['result']['item']['id'], 'lib': response['result']['item']['lib']}])


# print propDict[2]




        # p.append(response)
        # print response
# print jsonify(propDict[1])


# props = page.xpath('/html/body/div/div[2]/table/tbody/tr/td/text()')
# prop_info = page.xpath('//option/@value')
# / html / body / div / div[2] / table / tbody / tr[1] / td[1]
# propDict = defaultdict()
# propDict = []
# for i in range(0, len(propID)):
#     # propDict[prop[0]] = [prop[1]]
#     # for p in prop:
#     # print prop.xpath('//text()')
#         # print propID[i], propMeaning[i], propType[i], propValue[i] 
#         # try:
#         #     message = propID[i], propMeaning[i], propType[i], propValue[i]
#         # except:
#         #     print 'Broken',
#         message =  propID[i], propMeaning[i], propType[i]
#         propDict.append(message)

# for i in propValue:
#     print i



    # print prop
    # propDict.append(prop)
# term_list = []
# for i in xrange(0, len(terms)):
#     term_list.append({'value': term_ids[i], 'term': terms[i]})
#
# if return_list:
#     return term_list

# response = requests.get(self.baseurl + 'doc/requisitions', auth=(self.client, self.password))
# rawReqForm = html.fromstring(response.content)

# print propDict[30]
# return