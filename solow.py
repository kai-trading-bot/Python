from __future__ import division
import numpy as np

class Solow:
    def __init__(self,n,s,d,alpha,z,k):
        self.n, self.s,self.d, self.alpha, self.z=n, s,d,alpha,z
        self.k=k
        
    def h(self,x):
        temp = self.s*self.z*self.k**self.alpha+self.k*(1-self.d)
        return temp/(1+self.n)
    def update(self):
        self.k=self.h(self.k)
    def steady_state(self):
        return ((self.s*self.z)/(self.n+self.d))**(1/(1-self.alpha))
    def generate_sequence(self,t):
        path=[]
        for i in range(t):
            path.append(self.k)
            self.update()
        return path
    
    
import matplotlib.pyplot as plt
baseline_params=0.05, 0.25, 0.1, 0.3,2.0,1.0
s1=Solow(*baseline_params)
s2=Solow(*baseline_params)
s2.k=8
T=60
fig,ax=plt.subplots()
ax.plot([s1.steady_state()]*T,'k-',label='steady state')

for s in s1,s2:
    lb='Capital Series from Initial State{}'.format(s.k)
    ax.plot(s.generate_sequence(T),'o-',lw=2, alpha=0.6, label=lb)
    
ax.legend(loc='lower right')
plt.show()