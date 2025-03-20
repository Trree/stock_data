import baostock as bs

def get_top_50_code():
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)
    # 获取上证50成分股
    rs = bs.query_sz50_stocks()
    print('query_sz50 error_code:' + rs.error_code)
    print('query_sz50  error_msg:' + rs.error_msg)
    result_list = []
    for data in rs.data:
        result_list.append(data[1])
    # 登出系统
    bs.logout()
    return result_list




