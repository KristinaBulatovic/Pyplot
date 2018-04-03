from scipy.interpolate import spline
import numpy as np
import matplotlib.pyplot as plt
import pylab


x1 = []
y1 = []

x2 = []
y2 = []


for i in np.arange(1.0, 2.1, 0.1):
    x1.append(i)
    y1.append(0.5)


for j in np.arange(1.0, 2.1, 0.1):
    x2.append(j)
    y2.append(1/j)

# for i in np.arange(0.0, 1.1, 0.1):
#     x1.append(i)
#     y1.append(i**2)
#
#
# for i in np.arange(0.0, 1.1, 0.1):
#     x2.append(i)
#     y2.append(np.math.sqrt(i))

# xl=[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
# yl=[10.0, 4.44, 2.5, 1.6, 1.11, 0.82, 0.62, 0.49, 0.4, 0.33]


x_f1 = np.array(x1)
y_f1 = np.array(y1)
xnew_f1 = np.linspace(x_f1.min(),x_f1.max(),50)
ynew_f1 = spline(x_f1,y_f1,xnew_f1)

x_f2 = np.array(x1)
y_f2 = np.array(y1)
xnew_f2 = np.linspace(x_f2.min(),x_f2.max(),50)
ynew_f2 = spline(x_f2,y_f2,xnew_f2)

plt.subplot(311)
plt.plot(x1,y1,'bo',x1,y1,'k')

plt.subplot(311)
plt.plot(x2,y2,'bo',x2,y2,'k')

plt.title('Grafik funkcije y(x)')
# #plt.xlabel('x axis')
# plt.ylabel('y osa')
# plt.grid(True)
# plt.subplot(312)
# plt.plot(x1,y1,'r--')
# #plt.title('Plot of y vs. x')
# #plt.xlabel('x axis')
# plt.ylabel('y osa')
# plt.grid(True)
# plt.subplot(313)
# plt.plot(xnew,ynew)
#plt.title('Plot of y vs. x')
plt.xlabel('x osa')
plt.ylabel('y osa')
plt.grid(True)
plt.show()