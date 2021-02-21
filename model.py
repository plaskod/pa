import numpy as np
import matplotlib.pyplot as plt


def UAR(h_docelowe):
    """ ZBIORNIK """
    R = 1000                 # promien podstawy walca [metry]
    H = 500                # wysokosc walca [metry]
    A = np.pi * R * R     # pole podstawy walca [metry^2]
 
    """ DZIURA """
    
    max_r = 400                # promień dziury [metry]
    max_A_d = np.pi * max_r * max_r    # pole dziury [metry^2]

    r=0
    r_list=[]
    r_list.append(r)



    """ CZAS """
    t = 0                 # czas
    tsim = 1000           # czas symulacji
    Tp = 0.1              # krok czasu

    """ CONST """
    g = 9.80665           # przyspieszenie ziemskie [metry/sekunda^2]
    C = np.sqrt(2*g)/A     # stala odplywu
    
    """ DOPLYW """
    Q_d = 100               # doplyw poczatkowy [metry^3/sekunda]

    """ WYSOKOSC WODY """
    h_0 = 100               # poczatkowa wysokosc wody w zbiorniku
    h=[h_0]                  # lista wysokosci wody


    """ PID """
    Kp = 1.1636          # wzmocnienie regulatora
    Ki = 0.01            # stała czasu całkowania
    Kd = 1.3626          # stała czasu różniczkowania
    e_list=[0,0]
    u_list=[0,0]
    
    while t <= tsim:
        e_list.append(h_docelowe - h[-1])
        u = Kp * e_list[-1] + Ki * sum(e_list) + Kd * (e_list[-1] - e_list[-2])
        u_list.append(u)
        r = u

        A_d= np.pi * r * r
        h_n1 = 1/A * (Q_d - A_d*A_d * np.sqrt(h[-1]) * C) * Tp + h[-1]   # h(n+1)
        if(h_n1<0):
            h_n1=0
        h.append(h_n1)
        t += Tp
    return h

h_docelowe=60
h_list= UAR(h_docelowe)
fig, ax = plt.subplots()
ax.plot(h_list)
ax.hlines(y=h_docelowe, xmin=0, xmax=len(h_list), colors='red')
ax.set(xlabel='czas t', ylabel='wysokosc h', title='h(t)')
ax.grid()
plt.show()