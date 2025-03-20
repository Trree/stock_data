import baostock as bs

def get_top_code(query_type : int):
    # 登陆系统
    global rs
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)
    # 获取上证50成分股

    if query_type == 0:
        rs = bs.query_sz50_stocks()
    elif query_type == 1:
        rs = bs.query_hs300_stocks()
    if rs.error_code != 0 :
        print('query_sz50 error_code:' + rs.error_code)
        print('query_sz50  error_msg:' + rs.error_msg)
    result_list = []
    for data in rs.data:
        result_list.append((data[1], data[2]))
    # 登出系统
    bs.logout()
    return result_list




