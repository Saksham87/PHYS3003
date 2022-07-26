import csv
import math
import matplotlib.pyplot as plt

Phase= []
BV= []
with open('B-V.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        Phase.append(float(row[0]))
        BV.append(float(row[1]))
        

# plt.scatter(Phase,BV)
# plt.show()
# print(BV)
Temp=[]
for i in range(len(BV)):
    x=BV[i]
    if x > -0.0413:
        T = 10**((14.551-x)/3.684)
    else:
        T= 10**(4.945-math.sqrt(2.90698*x+1.08735))
    Temp.append(T)
plt.plot(Phase[1:],Temp[1:])
plt.xlabel("Phase")
plt.ylabel("Temperature (K)")
plt.savefig("Temp")
plt.show()
# print(Temp)
# To get bol Lumin.
Lum=[]
rad=[]
for T in Temp:
    y=math.log10(T)-4
    BC=-8.499*(y**4)+13.421*(y**3)-8.131*(y**2)-3.901*(y)-0.438
    Mbol=BC+9.90
    L=10**((4.74-Mbol)/2.5)*3.828*(10**26)
    Lum.append(L)
    r=math.sqrt(L/(T**4*5.67*(10**-8)*4*math.pi))
    rad.append(r)

plt.plot(Phase[1:],rad[1:])
plt.xlabel("Phase")
plt.ylabel("Radius (m)")
plt.savefig("Rad")
plt.show()