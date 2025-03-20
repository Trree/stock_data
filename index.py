import akshare.stock_feature.stock_a_pe_and_pb as sf

result_list = []
stock_market_pe_lg_df = sf.stock_market_pe_lg(symbol="上证")
result_list.append(stock_market_pe_lg_df[0])

stock_market_pe_lg_df = sf.stock_market_pe_lg(symbol="科创版")
result_list.append(stock_market_pe_lg_df[0])

for item in {"上证", "深证", "创业板", "科创版"}:
    stock_market_pe_lg_df = sf.stock_market_pe_lg(symbol=item)
    result_list.append(stock_market_pe_lg_df[0])

stock_index_pe_lg_df = sf.stock_index_pe_lg(symbol="上证50")
print(stock_index_pe_lg_df)

for item in [
    "上证50",
    "沪深300",
    "上证380",
    "创业板50",
    "中证500",
    "上证180",
    "深证红利",
    "深证100",
    "中证1000",
    "上证红利",
    "中证100",
    "中证800",
]:
    stock_index_pe_lg_df = sf.stock_index_pe_lg(symbol=item)
    result_list.append(stock_market_pe_lg_df[0])

for item in {"上证", "深证", "创业板", "科创版"}:
    stock_market_pb_lg_df = sf.stock_market_pb_lg(symbol=item)
    print(stock_market_pb_lg_df)

for item in [
    "上证50",
    "沪深300",
    "上证380",
    "创业板50",
    "中证500",
    "上证180",
    "深证红利",
    "深证100",
    "中证1000",
    "上证红利",
    "中证100",
    "中证800",
]:
    stock_index_pe_lg_df = sf.stock_index_pb_lg(symbol=item)
    result_list.append(stock_market_pe_lg_df[0])