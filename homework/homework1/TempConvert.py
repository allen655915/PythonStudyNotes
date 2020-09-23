# 输入摄氏温度或华氏温度转换为对应的华氏温度或摄氏温度
TempStr = input("请输入带有单位的温度值：")
if TempStr[0] in ['f','F']:
    C = (eval(TempStr[1:]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[0] in ['C','c']:
    F = (eval(TempStr[1:])*1.8+32)
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")