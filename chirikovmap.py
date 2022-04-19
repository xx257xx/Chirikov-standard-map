import matplotlib.pyplot as plt
import math
import numpy as np


for K in np.linspace(0.0, 1.0, 101):  
    fig = plt.figure(figsize=(50, 50))
    plt.axis('off')
    
    xs = []
    ps = []
    
    for k in range(49):
        for j in range(49):
            x = 0.02 + 0.02*j
            p = 0.02 + 0.02*k
            for i in range(300):
                xs.append(x)
                ps.append(p)
                p = p + (K/2*math.pi)*math.sin(2*math.pi*x)
                x = x + p
                p = p % 1.0
                x = x % 1.0
            

    plt.scatter(xs,ps,color='black')

    plt.savefig(str(K) + '.png')
