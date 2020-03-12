from pylab import plot,show
from numpy import linspace,sin,cos
from pylab import loadtxt
from pylab import plot,show,xlim,ylim
x=linspace(0,10,100)
y=sin(x)
ylim(-1.1,1.1)
g=cos(x)
plot(x,y)
plot(x,g)
show()

a=open("grafic.txt","w")
for i in range(len(x)):
     a.write("%.2f%.2f\n"%(x[i],y[i]))
a.close()

b=loadtxt("grafic.txt",float)
print(b[:0])
print(b[:1])

