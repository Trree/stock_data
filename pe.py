import baostock as bs
from tabulate import tabulate
from datetime import datetime, timedelta

from sz50 import get_top_50_code


def get_stock_pe(code_list : list):
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y-%m-%d")
    today_date = today.strftime("%Y-%m-%d")
    #### 获取沪深A股估值指标(日频)数据 ####
    # peTTM    滚动市盈率
    # psTTM    滚动市销率
    # pcfNcfTTM    滚动市现率
    # pbMRQ    市净率
    result_list = []
    for code in code_list:
        rs = bs.query_history_k_data_plus(code,
                                          "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
                                          start_date=yesterday_date, end_date=today_date,
                                          frequency="d", adjustflag="3")
        print('query_history_k_data_plus respond error_code:' + rs.error_code)
        print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)
        result_list.append(rs.data)

    #### 登出系统 ####
    bs.logout()
    flattened_data = [item[0] for item in result_list]
    sorted_data = sorted(flattened_data, key=lambda x: float(x[3]))
    return sorted_data


if __name__ == '__main__':
    result = get_top_50_code()
    pe = get_stock_pe(result)
    headers = ["Date", "Code", "Price", "Col4", "Col5", "Col6", "Col7"]
    print(tabulate(pe, headers=headers, tablefmt="pretty"))