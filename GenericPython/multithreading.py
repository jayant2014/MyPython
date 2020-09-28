import threading
import math
import time

pi = math.pi

def calc_circumference(radii):
    print("Calculate circumference of circles...")
    for r in radii:
        time.sleep(1)
        circumference = 2*pi*r
        print('Circumference : ', circumference)

def calc_area(radii):
    print("Calculate area of circles...")
    for r in radii:
        time.sleep(1)
        area = pi*r*r
        print('Area : ', area)

radii = [2,3,4,5]

t = time.time()

t1= threading.Thread(target=calc_circumference, args=(radii,))
t2= threading.Thread(target=calc_area, args=(radii,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Time taken : ",time.time()-t)
