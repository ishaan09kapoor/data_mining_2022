import matplotlib.pyplot as plt
s_all=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
b_all=[8,9,10,11,12,13,14,15,16,17,18,19,20]
count=0
for b in b_all:
    r=int(160/b)
    f=[]
    for s in s_all:
        f.append(1-(1-s**b)**r)
    print(r,b, f[6])
    plt.subplot(int(len(b_all)/2)+1,2,count+1)
    plt.title('r='+str(r)+', b='+str(b))
    plt.plot(s_all, f)
    count=count+1
plt.show()        
