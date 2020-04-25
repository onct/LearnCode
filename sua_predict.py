import numpy as np
import requests
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import datetime as dt

parameter_k = None
parameter_r = None

# 获取历史数据：确诊人数数据


def get_confirmdata():
    url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%E7%BE%8E%E5%9B%BD&'
    response = requests.get(url)

    usa_day_list = response.json()['data']

    x_data_date = []
    y_data = []
    for item in usa_day_list:
        x_data_date.append(item['date'])
        y_data.append(item['confirm'])

    # month,day = usa_day_list[0]['date'].split('.')

    x_data = np.arange(0, len(y_data))
    return x_data, y_data

# 通过获取的确诊数据，进行拟合，求出Logistic方程中的参数


def fit_data():

    # Logistic方程
    def logistic_function(t, P0):
        exp_r = np.exp(t * parameter_r)
        return parameter_k * P0 * exp_r / (parameter_k + P0 * (exp_r - 1))

    # 遍历K的区间和r的区间
    K_range = np.arange(460000, 1000000, 1000)
    r_range = np.arange(0, 1, 0.01)
    # 表示一个正无穷大数
    loss = float('inf')
    optimal_K = None
    optimal_r = None
    optimal_P0 = None
    x_data, y_data = get_confirmdata()
    print('x：', x_data)
    print('y：', y_data)

    i = 0
    for K_ in K_range:
        for r_ in r_range:
            parameter_k = K_
            parameter_r = r_

            popt, pcov = curve_fit(logistic_function, x_data, y_data)
            # print(y_data.dtype)
            # 找出最优的一次（最优的K和最优的r），让logistic_function最符合预测
            loss_ = mean_squared_error(y_data, logistic_function(x_data, popt))

            # 找到最小的 loss
            if loss_ < loss:
                loss = loss_
                optimal_K = K_
                optimal_r = r_
                optimal_P0 = popt

            i += 1

            # 拟合进度：▉▉▉▉42%
        print('\r拟合进度：{0}{1}%'.format('▉' * int(10 * i / len(K_range) /
                                                len(r_range)), int(100 * i / len(K_range) / len(r_range))), end='')
    print('\noptimal_K: ', optimal_K)
    print('optimal_r: ', optimal_r)
    print('optimal_P0: ', optimal_P0)

    parameter_k = optimal_K
    parameter_r = optimal_r
    return parameter_k, parameter_r, optimal_P0

# 进行预测，把未来的天数输入到预测模型中，获取天数对应的预测确诊数


def pred_data():

    x_data_predict = np.arange(0, 100)

    parameter_k, parameter_r, optimal_P0 = fit_data()
    print(optimal_P0)

    exp_r = np.exp(x_data_predict * parameter_r)
    y_data_predict = parameter_k * optimal_P0 * \
        exp_r / (parameter_k + optimal_P0 * (exp_r - 1))
    y_data_predict = y_data_predict.astype('int64')
    print('y_data_predict: ', y_data_predict)
    return y_data_predict

# 可视化


def view_pic():

    url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%E7%BE%8E%E5%9B%BD&'
    response = requests.get(url)

    usa_day_list = response.json()['data']
    month, day = usa_day_list[0]['date'].split('.')
    x_data_date, y_data = get_confirmdata()

    # 2020-01-28 字符串 转成 datetime
    first_date = dt.datetime.strptime('2020-' + month + '-' + day, '%Y-%m-%d')
    x_data_predict_date = [
        (first_date + (dt.timedelta(days=i))).strftime("%m.%d") for i in range(100)]
    y_data_predict = pred_data()

    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 画布大小
    plt.figure(figsize=(20, 10), dpi=400)
    # 预测确诊
    plt.plot(x_data_predict_date, y_data_predict,
             linewidth='1.5', color='red', label='预测确诊')
    # 现实确诊
    plt.scatter(x_data_date, y_data, s=35, color='m', label='实际确诊')

    # 显示图例，指定位置
    plt.legend(loc='upper left')
    plt.xticks(rotation=60)

    # 显示网格
    plt.grid()

    plt.ylabel('确诊人数')
    plt.savefig('usa_predict.png', dpi=300)
    plt.show()


view_pic()
