import baostock as bs

from query_type import QueryType


def get_top_code(query_type):
    # 登陆系统
    global rs
    lg = bs.login()
    # 显示登陆返回信息
    if lg.error_code != 0 :
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)

    if query_type == QueryType.SZ50:
        rs = bs.query_sz50_stocks()
    elif query_type == QueryType.HS300:
        rs = bs.query_hs300_stocks()
    if rs.error_code != 0 :
        print('get_top_code error_code:' + rs.error_code)
        print('get_top_code  error_msg:' + rs.error_msg)
    result_list = []
    for data in rs.data:
        result_list.append((data[1], data[2]))
    # 登出系统
    bs.logout()
    return result_list




