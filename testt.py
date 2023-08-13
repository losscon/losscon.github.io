# import pandas as pd
#
# file = 'example.xlsx'  # 第一行放金标准，第二行放AI结果
# line, row = 0, 0
# qingxidu = 0
# tp, tn, fp, fn = 0, 0, 0, 0
# data = pd.read_excel(file, sheet_name='Sheet1', engine='openpyxl', header=None)  # header=None表示不跳过首行
# # print(data.iloc[2,0]) #打印第一行第三列数据
# max_line = data.shape[0]  # 最大行
# max_row = data.shape[1]  # 最大列
# #######计算########
# # for j in range(5):
# #     for i in range(max_line):
# #         value = data.iloc[line, row]
# #         value1 = data.iloc[line, row + 1]
# #         if value == qingxidu:
# #             if value1 == qingxidu:
# #                 tp += 1
# #             else:
# #                 fn += 1
# #         else:
# #             if value1 == qingxidu:
# #                 fp += 1
# #             else:
# #                 tn += 1
# #         line += 1
# #     print(tp, tn, fp, fn)
# #     accuracy=(tp+tn)/(tp+tn+fp+fn)#准确率
# #     precision = tp/(tp+fp)#精确率
# #     recall = tp/(tp+fn)#召回率
# #     f1=(2*precision*recall)/(precision+recall)#f1分数
# #     print(qingxidu,accuracy,precision,recall,f1)
# #     qingxidu+=1
# #     tp, tn, fp, fn = 0, 0, 0, 0
# #     line, row = 0, 0
# #######计算########
# # a, b, c, d, e = 0, 0, 0, 0, 0
# # for i in range(5):
# #     for j in range(max_line):
# #         value = data.iloc[line, row]
# #         value1 = data.iloc[line, row + 1]
# #         if value == qingxidu:
# #             if value1 == 0:
# #                 a += 1
# #                 line += 1
# #             elif value1 == 1:
# #                 b += 1
# #                 line += 1
# #             elif value1 == 2:
# #                 c += 1
# #                 line += 1
# #             elif value1 == 3:
# #                 d += 1
# #                 line += 1
# #             elif value1 == 4:
# #                 e += 1
# #                 line += 1
# #         else:
# #             line += 1
# #     print(a,b,c,d,e)
# #     a, b, c, d, e = 0, 0, 0, 0, 0
# #     qingxidu += 1
# #     line=0
# ############计算RMSE########
# sum=0
# rmse=0
# for i in range(max_line):
#          value = data.iloc[line, row]
#          value1 = data.iloc[line, row + 1]
#          sum+=(value1-value)^2
# rmse=(1/max_line)*sum
# print(sum,rmse)


# import pandas as pd
# import numpy as np
#
# # 读取 xlsx 文件中的两列数据
# df = pd.read_excel('example.xlsx', usecols=[0, 1])
#
# # 计算均方根误差
# rmse = np.sqrt(((df.iloc[:, 0] - df.iloc[:, 1]) ** 2).mean())
# print(rmse)


import pandas as pd


# 读取excel每一个Sheet的每一个单元格，输出所有非中文字符并统计出现次数
def write_excel_to_txt(excel_file, txt_file):
    # Read excel file
    excel_data = pd.read_excel(excel_file, sheet_name=None)

    # Open txt file in write mode
    with open(txt_file, 'w', encoding='utf-8') as file:
        # Iterate over each sheet in the excel file
        for sheet_name, sheet_data in excel_data.items():
            # Iterate over each row in the sheet
            for index, row in sheet_data.iterrows():
                # Write each row to the txt file
                file.write('\t'.join([str(value) for value in row]) + '\n')


# 读取txt文件，输出txt文件中所有非中文字符并统计次数，输出到新的txt文件
def read_and_count_non_chinese_characters(input_file, output_file):
    # Open the input file in read mode
    with open(input_file, 'r',encoding='utf-8') as file:
        # Read the contents of the file
        content = file.read()

    # Initialize a dictionary to store the count of each non-Chinese character
    count_dict = {}

    # Iterate over each character in the content
    for char in content:
        # Check if the character is non-Chinese
        if not is_chinese(char):
            # Increment the count of the character in the dictionary
            count_dict[char] = count_dict.get(char, 0) + 1

    # Open the output file in write mode
    with open(output_file, 'w',encoding='utf-8') as file:
        # Iterate over each character and its count in the dictionary
        for char, count in count_dict.items():
            # Write the character and its count to the output file
            file.write(f"{char}: {count}\n")


def is_chinese(char):
    # Check if the character is a Chinese character
    # You can implement your own logic here to determine if a character is Chinese or not
    # For simplicity, let's assume all Chinese characters have Unicode code points greater than 128
    return ord(char) > 128


# 读取txt文件，输出txt文件中所有非中文字符并统计次数，输出到excel
# write_excel_to_txt('X线检查数据1.xlsx', 'XDataset.txt')
# 读取txt文件，输出txt文件中所有非中文字符并统计次数，输出到新的txt文件
# read_and_count_non_chinese_characters("XDataset.txt", "XNoChinese.txt")

