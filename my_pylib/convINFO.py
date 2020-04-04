import re
import requests
import json
import matplotlib.pyplot as plt
from pyecharts.charts import Bar,Line
from pyecharts import options as opts


class convINFO:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36 Edg/83.0.461.1'
        }

    # 发送请求，获取数据
    def getHTMLText(self):
        try:
            r = requests.get(url=self.url, headers=self.headers, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            data = r.json()
            data_list = data.get('children')
            data_dict = json.loads(data['data'])
            return data_dict
        except:
            return ''

    # 解析数据
    def getProvinceInfo(self, data_dict):
        # 获取省份列表数据
        data_list = data_dict['areaTree'][0]['children']
        provinceInfo_list = []
        for result in data_list:
            info_dict = {}
            info_dict['name'] = result['name']
            info_dict['confirm'] = result['total']['confirm']
            provinceInfo_list.append(info_dict)
        return provinceInfo_list

    def getDailyInfo(self, data_dict):
        # 获取每日数据
        data_list = data_dict['chinaDayList']
        for result in data_list:
            month, day = result['date'].split('.')
            date = '2020-%s-%s' % (month, day)
            result['date'] = date
        return data_list

    def barinfoChart(self, data_list):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        province_list = []
        confirm_list = []
        for i in range(10):
            province_list.append(data_list[i]['name'])
            confirm_list.append(data_list[i]['confirm'])
        bar = Bar()
        bar.add_xaxis(province_list)
        bar.add_yaxis("累计确诊数", confirm_list)
        bar.set_global_opts(title_opts=opts.TitleOpts(title="全国各省确诊情况"))
        bar.render()

    def lineInfoChart(self, data_list):
        date_list=[]
        confirm_list=[]
        dead_list=[]
        heal_list=[]
        nowConfirm_list=[]
        for result in data_list:
            date_list.append(result['date'])
            confirm_list.append(result['confirm'])
            dead_list.append(result['dead'])
            heal_list.append(result['heal'])
            nowConfirm_list.append(result['nowConfirm'])
        line = (
            Line()
            .add_xaxis(date_list)
            .add_yaxis(
            series_name="累计确诊人数",
            is_smooth=True,
            is_symbol_show=False,
            color="#DD2222",
            y_axis=confirm_list
            )
            .add_yaxis(
            series_name="死亡人数",
            is_smooth=True,
            is_symbol_show=False,
            color="#778877",
            y_axis=dead_list
            )
            .add_yaxis(
            series_name="治愈人数",
            is_smooth=True,
            is_symbol_show=False,
            color="#22DDB8",
            y_axis=heal_list
            )
            .add_yaxis(
            series_name="剩余确诊人数",
            is_smooth=True,
            is_symbol_show=False,
            color="#4DB3B3",
            y_axis=nowConfirm_list
            )
            
            .set_global_opts(title_opts=opts.TitleOpts(title="nConv疫情变化趋势图"))
            .render("line_base.html")
        )

    def run(self):
        # 1、构建请求头和url
        # 2、发送请求，获取数据
        data_dict = self.getHTMLText()
        data_list=self.getDailyInfo(data_dict)
        self.lineInfoChart(data_list)
        # 3、解析数据
        # data_list = self.getProvinceInfo(data_dict)
        # self.barinfoChart(data_list)


if __name__ == '__main__':
    # url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'

    conv_Info = convINFO(url)
    conv_Info.run()
