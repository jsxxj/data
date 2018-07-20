import matplotlib.pyplot as plt 
x1=range(2,11) 
x2=range(2,11) 
x3=range(2,11)
y1=[0.997,0.99,0.997,0.94,0.94,0.973,0.977,0.98,1] 
y2=[0.991,0.996,0.994,0.972,0.994,0.989,0.946,0.959,0.961] 
y3=[0.824,0.948,1,0.896,0.876,0.864,0.958,0.982,0.956]

plt.plot(x1,y1,label='olivettiFaces',linewidth=2,color='r',marker='o', 
markerfacecolor='blue',markersize=6) 
plt.plot(x2,y2,label='JAFFE',linewidth=2,color='b',marker='<', 
markerfacecolor='blue',markersize=6) 
plt.plot(x3,y3,label='Tseries-class',linewidth=2,color='y',marker='>', 
markerfacecolor='blue',markersize=6) 
plt.xlabel('class') 
plt.ylabel('accuracy') 
#plt.title('Interesting Graph\nCheck it out') 
plt.legend() 
plt.ylim(0.0,1.4)
plt.show() 
plt.savefig('accuracy.png')
