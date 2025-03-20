import akshare.stock_feature.stock_a_indicator as stock_a_indicator
import time
from sz50 import get_top_50_code


def get_all_pe_info(code_list: list):
    result_list = []
    for stock_code in code_list:
        try:
            indicator_df = stock_a_indicator.stock_a_indicator_lg(symbol=stock_code)
            columns_pe = indicator_df[['pe', 'pe_ttm', 'pb']]
            result_list.append([stock_code] + columns_pe.tail(1).values.flatten().tolist())
            time.sleep(0.2)
        except Exception as e:
            print(e)
            pass
    return result_list

if __name__ == '__main__':
    result = get_top_50_code()
    pe = get_all_pe_info(result)
    pe.sort(key=lambda x: x[1])
    print(pe)