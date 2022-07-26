# file = open('Combined Light Curve - B.txt','r')
xval=[]
yval=[]
# for x, line in enumerate(file):
#     if x>1:
#         l=line.split(' ')
#         if float(l[1]) <99:
#             xval.append(float(l[0]))
#             yval.append(float(l[1]))

file2 = open('Vdata.txt','r')
for x, line in enumerate(file2):
    if x>0:
        l=line.split('\t\t')
        xval.append(float(l[0]))
        yval.append(float(l[1]))

# print(xval)
# print(yval)

zipped = zip(xval, yval)
ordered = sorted(zipped, key = lambda x:x[0])
unzipped = list(zip(*ordered))
a = unzipped[0]
b = unzipped[1]
print(ordered)
import matplotlib.pyplot as plt

# plt.scatter(xval,yval,color='black')
# 
# plt.show()
import scipy
from scipy.interpolate import interp1d as inter
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
# out = scipy.interpolate.CubicSpline(a, b, axis=0)
print(a)
data= [a,b]
tck,u = interpolate.splprep(data, s=0.4)
unew = np.arange(0,1, 0.01)
out = interpolate.splev(unew, tck)
plt.figure()
plt.scatter(out[0], -out[1]-9.90, color='orange')
# plt.plot(data[0], data[1], 'ob')
plt.show()

def fV(x):
    tck = interpolate.splrep(a,b, s=0.4)
    return interpolate.splev(x, tck)

##

xval=[]
yval=[]
file2 = open('Bdata.txt','r')
for x, line in enumerate(file2):
    if x>0:
        l=line.split('\t\t')
        xval.append(float(l[0]))
        yval.append(float(l[1]))

zipped = zip(xval, yval)
ordered = sorted(zipped, key = lambda x:x[0])
unzipped = list(zip(*ordered))
c = unzipped[0]
d = unzipped[1]

def fB(x):
    tck = interpolate.splrep(c,d, s=0.1)
    return interpolate.splev(x, tck)
Vmags=[]
Bmags=[]

for val in unew:
    Vmags.append(-fV(val))

for val in unew:
    Bmags.append(-fB(val))
    
plt.plot(unew,Vmags, label="V")
plt.plot(unew,Bmags, color='red',label="B")
plt.legend(loc="upper right")
plt.xlabel("Phase")
plt.ylabel("Mag (Instrumental)")
plt.savefig("B and V")
plt.show()

BV=[]

for val in unew:
    BV.append(-((fB(val)+9.99)-(fV(val)+9.90)))
# ax = plt.gca()
# ax.invert_yaxis()

plt.plot(unew[1:],BV[1:])
plt.xlabel("Phase")
plt.ylabel("B-V")
plt.savefig("B-V")
plt.show()

import csv

with open('B-V.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)

    for i in range(len(unew)):
        writer.writerow([unew[i],BV[i]])

# import csv
# rows = zip(out[0],out[1])
# 
# # open the file in the write mode
# with open('Vforcurve.csv', 'w', newline='') as f:
#     # create the csv writer
#     writer = csv.writer(f)
# 
#     # write a row to the csv file
#     for row in rows:
#         writer.writerow(row)





# import csv
# 
# with open('UU Vir-B and V data.csv', 'w', encoding='UTF8',newline='') as f:
#     writer = csv.writer(f)
# 
#     for i in range(len(xval)):
#         writer.writerow([xval[i],yval[i]])