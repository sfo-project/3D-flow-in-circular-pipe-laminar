#Just to know last time this was run:
import time
import numpy as np
import matplotlib.pyplot as plt

print time.ctime ()
print "\n"

#---Flow conditions (begin)---
R=0.05		#Pipe radius in [m]
U0=0.01		#Free stream velocity in [m/s]
rho=1		#Fluid density in [kg/m3]
mu=1.7894E-5	#Fluid viscosity [kg/m-s]
#---Flow conditions (end)---


#---Calculating the flow field parameters (begin)---

#Determine flow regime using Reynolds ceriteria
Re=(rho*U0*2*R)/mu
print "Reynolds number is: %d [-]" % Re 

if Re < 2000:
  print "Your pipe flow is LAMINAR"
  print "\n"
elif 2000 <= Re <= 4000:
  print "Your pipe flow is Transitional"
  print "\n"
else:
  print "Your pipe flow is Turbulent"
  print "\n"

#Determine entrance length

if Re < 2000:
  le = (0.06*Re) * (2*R)
  print "The entrance length of the flow is: %f [m]" % le 
  print "\n"
else:
  le = (4.4*Re^1.6) * (2*R)
  print "The entrance length of the flow is: %f [m]" % le 
  print "\n"
#---Calculating the flow field parameters (end)---

#---Post-process CFD data (begin)---
datafile = open('velocity_field_140000_elements.txt', 'r')

data = []
comments = []

header_read = False
for row in datafile:
    if row[0] != '(' and row[0] != ')' and row[0] != '\n' : # comment lines are skipped
        if not header_read:
            header = row
            header_read = True # next time, data will be read
        else:
            data.append(row)
    else:
        comments.append(row)
datafile.close()


zList = []
vList = []

for row in data:
  z = [s.split() for s in row.splitlines()][0][0]
  v = [s.split() for s in row.splitlines()][0][1]
  zList.append(float(z))
  vList.append(float(v))

#from pprint import pprint
#pprint(zList)
#pprint(vList)

zList_norm = []
zList_norm= [x/R for x in zList]
vList_norm = []
vList_norm= [x/U0 for x in vList]

plt.figure(1)

plt.plot(vList_norm[0:50],zList_norm[0:50],'ro', label='1D')          
plt.plot(vList_norm[50:100],zList_norm[0:50],'bo', label='3D')	
plt.plot(vList_norm[100:150],zList_norm[0:50],'go', label='25D')	
plt.plot(vList_norm[150:199],zList_norm[150:199],'k+', label='45D')	

plt.legend( loc='upper right', numpoints = 1 )
plt.xlabel('u/U0')
plt.ylabel('r/R')
#---Post-process CFD data (end)---


#---CFD data validation (begin)---
u_r_norm=[]

u_r_norm=[( max(vList)*(1-x**2) )/U0 for x in zList_norm]

plt.figure(2)
plt.plot(vList_norm[100:150],zList_norm[0:50],'go', label='CFD (25D)')
plt.plot(u_r_norm[0:51],zList_norm[0:51],'x--', label='Theoretical')

plt.legend( loc='upper right', numpoints = 1 )
plt.xlabel('u/U0')
plt.ylabel('r/R')
#---CFD data validation (end)---

plt.show() #This prints all the figures in the end.