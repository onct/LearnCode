# eastmoney stock crawler
# tools browser Developer Tools
import requests

def getHTMLText(url,headers):
    try:
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.json()
    except:
        return "123"


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36 Edg/83.0.461.1'
    }

    url = 'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=QGQP_LB&token=70f12f2f4f091e459a279469fe49eca5'
    
    html = getHTMLText(url,headers)
    print(type(html))
    result_list=[]
    for data_dict in html:
        temp={}
        temp['Code']=data_dict['Code']
        temp['Name']=data_dict['Name']
        temp['JGCYDType']=data_dict['JGCYDType']
        temp['ChangePercent']=data_dict['ChangePercent']
        result_list.append(temp)
    print (result_list)
        

