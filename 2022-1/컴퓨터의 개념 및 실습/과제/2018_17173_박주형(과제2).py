time=input("시간(0-23)과 분(0-59)을 입력하시오: ")
time=time.split()
hour=int(time[0])
min=int(time[1])
if min>=45:
    print(hour,min-45)

elif hour!=0:
    print(hour-1,min+15)

else: print(23, min+15)