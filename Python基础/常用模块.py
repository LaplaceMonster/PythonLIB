from datetime import datetime, timedelta #该模块包含一个datetime类，这个类使我们要用的时间相关的函数更加简单
now = datetime.now() #获取当前时间
print(now)
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
#datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print(now-timedelta(hours=10))
print(now+timedelta(days=1))
#datetime加减：可以直接对时间进行加减运算来求出时间差
