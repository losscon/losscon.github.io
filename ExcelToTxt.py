# import openpyxl
# import re
#
# # 打开excel
# workbook = openpyxl.load_workbook('file.xlsx', data_only=True)
# sheet_names = workbook.sheetnames
#
# # 读取所有sheet
# for sheet_name in sheet_names:
#     # Select the sheet
#     sheet = workbook[sheet_name]
#
#     # Get the maximum row and column count
#     max_row = sheet.max_row
#     max_column = sheet.max_column
#
#     # Loop through each cell
#     for row in range(1, max_row + 1):
#         for column in range(1, max_column + 1):
#             # Get the cell value
#             cell_value = sheet.cell(row=row, column=column).value
#             # Check if the cell is not empty
#             if cell_value is not None:
#                 cell_value = cell_value.rstrip('\n')
#                 # 去掉空格
#                 cell_value = re.sub("(?:\u0020|\u3000|\u00A0|\u2002|\u2003|\s+|_x000D_)", "", cell_value)
#
#                 # 英文小写
#                 # cell_value = cell_value.lower()
#                 # 去除符号
#                 symbols = [",", "!", "?", ";", ":", "，", "；", ".", "？", "；", "，", "、"]
#                 for symbol in symbols:
#                     cell_value = cell_value.replace(symbol, "。")
#
#                 # Write the cell value to a txt file
#                 with open('output.txt', 'a+', encoding='utf-8') as file:
#                     if cell_value not in file:
#                         file.write(cell_value + '\n')


import openpyxl
import re


def ExcelToTxt(excelname, txtname):
    # 打开excel
    workbook = openpyxl.load_workbook(excelname, data_only=True)
    sheet_names = workbook.sheetnames
    # 创建一个空的集合
    written_values = set()
    # 读取所有sheet
    for sheet_name in sheet_names:
        sheet = workbook[sheet_name]

        # Get the maximum row and column count
        max_row = sheet.max_row
        max_column = sheet.max_column

        # Loop through each cell
        for row in range(1, max_row + 1):
            for column in range(1, max_column + 1):
                # Get the cell value
                cell_value = sheet.cell(row=row, column=column).value
                # 如果单元格不为空
                if cell_value is not None:
                    cell_value = cell_value.rstrip('\n')
                    # 去掉空格
                    cell_value = re.sub("(?:\u0020|\u3000|\u00A0|\u2002|\u2003|\s+|_x000D_)", "", cell_value)
                    # 英文小写
                    cell_value = cell_value.lower()
                    # 去除符号
                    symbols = ["—", "(", "%", "●", "√", ")", "№", "✚", "﹣", "/", "＝", "\"", "／", "\'", "）", "．", "㎝",
                               "", "”", "+", "≤", "-", "＇", "∏", "[", "＃", "≈", "‘", "*", "#", "“", "", "′", "＊", "（",
                               "～", "", "’", "∽", "㎡", "÷", "°", "…", "】", "|", "－", "±", "℃", "％", "&", "@", "×", "□",
                               "·", "：", "‖", "≥", "^", "＜", "゜", "＋", "㎜", "=", ">", "`", "]", "！", "＞", "【", "﹤", "~",
                               "。", "<", "!", "?", ";", ":", "，", "；", ".", "？", "；", "，", "、", "\\", "》", "‹", "✖","️",
                               "■", "△", "♀", "○", "", "}", "↑", "︿", "。", ",", "﹀", "┳", "《", "▽", "", "", "＂", "›",
                               "﹑", "┺", "｝", "{", "〈", "※", "", "｛", "▏", ",", "¡", "＂", "《", "£", "¸", "﹑", "", ",",
                               "", "＼", "️", "》", "«", "■", "¨", "↑", "﹢", "¯", "»", "{", "�", "´", "}", "❌", "✖", "👆",
                               "¬", "→"]
                    for symbol in symbols:
                        cell_value = cell_value.replace(symbol, "。")
                    # 删除连续的句号
                    while "。。" in cell_value:
                        cell_value = cell_value.replace("。。", "。")
                    # 写入txt
                    with open(txtname, 'a+', encoding='utf-8') as file:
                        # 检查当前值是否在集合中
                        if cell_value not in written_values:
                            # 如果不在，就写入并添加到集合中
                            file.write(cell_value + '\n')
                            written_values.add(cell_value)
                        else:
                            # 如果在，就跳过
                            pass


ExcelToTxt('副本MR检查.xlsx', 'MRData.txt')
ExcelToTxt('副本X线检查数据.xlsx', 'XrayData.txt')
ExcelToTxt('副本CT检查信息.xlsx', 'CTData.txt')
