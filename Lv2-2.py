# Case1
a = 200000
day = 0         # 60*60*24
hour = 0
minute = 0
second = 0

day = a // (60*60*24)
hour = a % (60*60*24) // (60*60)
minute = a % (60*60*24) % (60*60) // 60
second = a % (60*60*24) % (60*60) % 60
print("%d %d %d %d" % (day, hour, minute, second))


# Case2
num = 200000
second = num

while(0<second-60):
    second-=60
minute = int((num-second)/60)
while(0<minute-60):
    minute-=60
hour = int((num-second-(minute*60))/3600)
while(0<hour-24):
    hour-=24
day = int((num-second-(minute*60)-(hour*3600))/86400)

print(day,hour,minute,second)
