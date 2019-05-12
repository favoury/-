# 批量替换文件夹内csv文件首行名称，选取需要列，重新写入新的文件夹内

import pandas as pd
import os
filePath = 'F:\date\stock_data' # 文件目录
filePath_name = os.listdir(filePath)
# print(filePath_name)


# 批量替换首行名称
# 循环列表
# for fp_name in filePath_name:
#     print(fp_name)
#
#     # 将文件读取到内存中
#     with open("F:\date\stock_data\\" + fp_name ,"r",encoding="gbk") as f:
#         lines = f.readlines()
#     # 写的方式打开文件
#     with open("F:\date\stock_data\\" + fp_name ,"w",encoding="gbk") as f_w:
#         # dict_name = {'code': '股票代码', 'date': '交易日期', 'open': '开盘价'}
#         dict_name = {'code': '股票代码', 'date': '交易日期', 'open': '开盘价', 'high': '最高价', 'low': '最低价', 'close': '收盘价', 'change': '涨跌幅', 'volume': '成交量', 'money': '成交额', 'traded_market_value': '流通市值', 'market_value': '总市值', 'turnover': '换手率', 'adjust_price': '后复权价', 'report_type': '财务报告类型', 'report_date': '财报发布日期', 'PE_TTM': '市盈率', 'PS_TTM': '市销率', 'PC_TTM': '实现率', 'PB': '市净率', 'adjust_price_f': '前复权价格'}
#
#         for line in lines:
#             for key in dict_name:
#                 # print(key)
#                 # print(dict_name[key])
#                 if key in line:
#                  # 替换
#                     line = line.replace(key,dict_name[key])
#             f_w.write(line)

# 处理原数据列，写入内存但未存储
for fp_name in filePath_name:
    pd.set_option('expand_frame_repr', False)  # 当列太多时显示完整
    df = pd.read_csv(
        filepath_or_buffer = 'F:\date\stock_data\\' + fp_name,
        encoding='gbk',
    )
    df = df[['股票代码', '交易日期', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '成交量', '成交额', '市净率', '总市值', '流通市值', '换手率']]
    # all_df = all_df.append(df, ignore_index=True)
    # df.reset_index(drop=True, inplace=True)

    print(df)
    print('数据处理' + fp_name)

# 对整理后的数据进行存储
    for i in df.index:
        t = df.iloc[i:i+1, :]
        stock_code = t.iloc[0]['股票代码']

        # 构建存储文件路径
        path = 'F:\date\\new_date\\' + fp_name
        # 文件存在，不是新股
        if os.path.exists(path):
            t.to_csv(path, header=None, index=False, mode='a', encoding='gbk')
        # 文件不存在，说明是新股
        else:
            # 先将头文件输出
            t.to_csv(path, index=False, mode='a', encoding='gbk')
        # print(df)
