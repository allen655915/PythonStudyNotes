height = float(input('请输入您的身高(米):'))
weight = float(input('请输入您的体重(千克):'))
bmi = weight / height ** 2# 计算BMI值
print('您的BMI值为：{:.1f}'.format(bmi))
if bmi <= 18.4:
    print('偏瘦')
elif bmi < 23.9:
    print('正常')
elif bmi < 27.9:
     print('过重')
else:
    print('肥胖')