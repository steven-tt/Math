import matplotlib.pyplot as plt
from random import randint
import math
import time

def serp_tri(pair):
    '''
    Input: a point in cartesain coordinates
    Output: a point in cartesain coordinates
    This takes in a point and finds the mid point between it and one of three other point.
    '''
    choice = randint(0,2)
    x = pair[0]
    y = pair[1]
    if choice == 0:
        x1,y1 = 0,0
    elif choice == 1:
        x1,y1 = .5, math.sqrt(1-.5**2)
    else:
        x1,y1 = 1,0
    return ((x+x1)/2,(y+y1)/2)


start = time.time()


my_list = [(0,0)]# start with any arbitrary point
x_list = []
y_list = []

#take starting point and run it through the function any number of times

count = 0
while count < 1000000-1:
    my_list.append(serp_tri(my_list[count]))
    count+=1

for (a,b) in my_list:
    x_list.append(a)
    y_list.append(b)

plt.figure(figsize=(20,20))
plt.plot(x_list,y_list,'o',markersize=.1)
# plt.savefig("Serpenski_Triangle.png")
plt.show()
plt.close()

print(f"{len(my_list)} points")
print(f"{time.time()-start:1.3f} seconds to complete")
