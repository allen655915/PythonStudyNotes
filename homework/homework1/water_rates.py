# coding=utf-8
# 第一阶梯水量为每户每年260m3及以下，水价按现行2.20元/ m3执行
# 第二阶梯水量为每户每年261—360 m3（含），水价在第一阶梯基础上加价0.66元/ m3，即2.86元/ m3
# 第三阶梯水量为361 m3及以上，水价在第一阶梯基础上加价2.20元/ m3，即4.40元/ m3
# 水价外代收水资源费0.10元/ m3、污水处理费1.00元/ m3
# 尚未安装“一户一表”的合表居民用户和执行居民生活用水价格的非居民用户，在第一阶梯水价基础上，加价0.10元/ m3，水价由2.20元/ m3调整为2.30元/ m3

# 数据输入函数
def confirm():
    print('请输入您本年度的用水量，如:270.45A')
    print('注：如果您是非“一户一表”的合表居民用户或执行居民生活用水价格的非居民用户请在用水量后加上字母B否则加上字母A')
    print('-------------------------------------------------------------------------------------------------')
    num = input("请输入:")
    transform(num)

# 水费计算函数
def compute(num,stan):
    if num <= 260:
        price = 2.2
        if stan == 'B':
            price = 2.3
    if num > 260 and num<=360:
        price = 2.86
        if stan == 'B':
            price = 2.96
    else:
        price = 4.4
        if stan == 'B':
            price = 4.5
    price = price + 1.1
    sum = num * price
    return sum

# 数据转换函数
def transform(num):
    stan = num[-1]
    num = float(num[0:-1])
    if stan in ['b','B']:
        print('您是非“一户一表”的合表居民用户或执行居民生活用水价格的非居民用户')
        print('您本年度的用水量为:{0:.2f}m³'.format(num))
        print('-----------------------------------------------------')
    elif stan in ['a','A']:
        print('您是“一户一表”的合表居民用户')
        print('您本年度的用水量为:{0:.2f}m³'.format(num))
    else:
        print('您的输入不符合规范！')
        confirm()
    print('请确认您的信息是否正确！')
    respond = input("返回请输入N,计算请输入Y:")
    if respond in ['y','Y']:
        sum = compute(num,stan)
        print('---------------------------------------')
        print("您本年度应缴水费为：{0:.2f}元".format(sum))
    else:
        confirm()

confirm()
