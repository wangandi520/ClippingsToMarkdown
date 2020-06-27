import time

clippingTime = float(1571131503114/1000) 
clippingTimeTransfered = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(clippingTime))
print(clippingTimeTransfered)