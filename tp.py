import pandas as pd
file = 'test3.xlsx'  # 第一行放金标准，第二行放AI结果
line, row = 0, 0
tp, tn, fp, fn = 0, 0, 0, 0
data = pd.read_excel(file, sheet_name='Sheet1', engine='openpyxl', header=None)
max_line = data.shape[0]  # 最大行
max_row = data.shape[1]  # 最大列
for i in range(max_line):
    value = data.iloc[line, row]
    value1 = data.iloc[line, row + 1]
    # print(value,value1)
    if value==1:
        if value1==value:
            tp+=1
        else:
            fn+=1
    elif value==0:
        if value1==value:
            tn+=1
        else:
            fp+=1
    line += 1
print(tp, fn, tn, fp)
precision = tp/(tp+fp)#精确率
recall = tp/(tp+fn)#召回率
f1=(2*precision*recall)/(precision+recall)#f1分数
print(tp,fn,tn,fp,precision,recall,f1)



# a=0
# with open('test4.txt', 'r',encoding='utf-8') as f:
#     for line in f:
#         a+=1
#         if len(line.split()) !=2:
#             print(a)

