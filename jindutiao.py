import time

for i in range(100000):
    percent = 1.0 * i / 100000 * 100

    print(percent)

    print('complete percent: %10.8s%s'%(str(percent),'%'),end='\r')


    time.sleep(0.1)
