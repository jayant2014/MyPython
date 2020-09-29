from multiprocessing import Process
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

p1 = Process(target=calc_circumference, args=(radii,))
p2 = Process(target=calc_area, args=(radii,))

p1.start()
p2.start()

p1.join()
p2.join()

print("Time taken : ",time.time()-t)
