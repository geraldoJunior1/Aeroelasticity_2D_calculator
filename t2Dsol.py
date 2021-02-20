import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA
import matplotlib.pyplot as plt
import math


def nestacionario(xcm,xf,s,ro,c,m,flex,tor):

    b=c/2
    e=xcm/b-1 
    a=xf/b-1
    t = 4/1000
    xtetha=e-a
    imag1=[]
    imag2=[]
    freq1u=[]
    freq2u=[]
    vk=[]
    vk2=[]

    freq1=flex*2*np.pi
    freq2=tor*2*np.pi

    mi=m/(ro*np.pi*b**2)
    Iz=(1/12)*m*(t**2+c**2)
    r=np.sqrt(Iz/(m*b**2))

    sigma=freq1/freq2

    k=0.3

    while k<15:

        ck=(0.01365+0.2808j*k-(k**2)/2)/(0.01365+0.3455j*k-k**2)
        lh=1-(2j*ck)/k
        ltetha=-a-(1j/k)-(2*ck)/(k**2)-(2j*(0.5-a)*ck)/k
        mh=-a+(2j*(0.5+a)*ck)/k
        mtetha=(1/8)+a**2-(1j*(0.5-a))/k+(2*(0.5+a)*ck)/k**2+(2j*(1/4-a**2)*ck)/k

        a03=-(mi*xtetha+mh)*(mi*xtetha+ltetha)
        a02=(mi**2*r**2)+(mi*mtetha)+(mi*r**2*lh)+(lh*mtetha)
        a0=a03+a02
        a1=-(mi**2*r**2)-(mi**2*sigma**2*r**2)-(mi*sigma**2*mtetha)-(mi*r**2*lh)
        a2=mi**2*sigma**2*r**2
        delta=np.sqrt(a1**2-4*a2*a0)
        x1=(-a1+delta)/(2*a2)
        x2=(-a1-delta)/(2*a2)
        imag1.append(np.imag(x1))
        imag2.append(np.imag(x2))

        freq1u.append(((1/np.sqrt(np.real(x1)))*freq2)/(2*np.pi))
        freq2u.append((1/np.sqrt(np.real(x2)))*freq2/(2*np.pi))
        vk.append((1/k)*freq2*b)
        vk2.append((1/k)*freq2*b)

        k=k+0.001

    return vk,imag1, vk2, imag2, vk,freq1u,vk2,freq2u
 

def autovalorcomplex(xcm,xf,s,rho,c,m,freq1,freq2,v2):
    

    e = xf/c - 0.25

    #e = xf/c - ca

    v1 = 1
    step = 0.1

    a = 2*np.pi
    rho = 1.225
    M_theta_dot = -1.2

    M = (m*c**2 - 2*m*c*xcm)/(2*xcm)

    z1 = 0.0
    z2 = 0.0
    w1 = freq1*2*np.pi
    w2 = freq2*2*np.pi
    alpha = 2*w1*w2*(-z2*w1 + z1*w2)/ (w1*w1*w2*w2)
    beta = 2*(z2*w2-z1*w1) / (w2*w2 - w1*w1)

    a11=(m*s**3*c)/3 + M*s**3/3
    a22= m*s*(c**3/3 - c*c*xf + xf*xf*c) + M*(xf**2*s)
    a12 = m*s*s/2*(c*c/2 - c*xf ) - M*xf*s**2/2
    a21 = a12

    A=np.zeros((2,2))
    A[0][0]=a11
    A[0][1]=a12
    A[1][0]=a21
    A[1][1]=a22


    k1 = (freq1*np.pi*2)**2*a11
    k2 = (freq2*np.pi*2)**2*a22



    E=np.zeros((2,2))
    E[0][0]=k1
    E[0][1]=0
    E[1][0]=0
    E[1][1]=k2

    C=np.zeros((2,2))
    K=np.zeros((2,2))

    A_special = alpha*A
    E_special = beta*E
    K_special = np.zeros((2,2))

    K_special[0][0] = k1
    K_special[0][1] = 0
    K_special[1][0] = 0
    K_special[1][1] = k2

    invAK = np.zeros((2,2))
    invAC = np.zeros((2,2))

    princp = np.zeros((4,4))

    princp[0][0] = 0
    princp[0][1] = 0
    princp[1][0] = 0
    princp[1][1] = 0

    princp[0][2] = 1
    princp[0][3] = 0
    princp[1][2] = 0
    princp[1][3] = 1

    V=0
    vel=[]
    frequen = np.zeros((0,4))
    amort = np.zeros((0,4))

    while V < v2:
        V=V+v1
        C[0][0] = c*s**3*a/6
        C[0][1] = 0
        C[1][0] = -c**2*s**2*e*a/4
        C[1][1] = -c**3*s*M_theta_dot/8
        C=rho*V*C+A_special+E_special
        K[0][0] = 0
        K[0][1] = c*s**2*a/4
        K[1][0] = 0
        K[1][1] = -c**2*s*e*a/2
        K = rho*V**2*K+K_special
        
        invAK = np.linalg.solve(-A, K)
        invAC = np.linalg.solve(-A, C)

        princp[2][0] = invAK[0][0]
        princp[2][1] = invAK[0][1]
        princp[3][0] = invAK[1][0]
        princp[3][1] = invAK[1][1]

        princp[2][2] = invAC[0][0]
        princp[2][3] = invAC[0][1]
        princp[3][2] = invAC[1][0]
        princp[3][3] = invAC[1][1]
        #print(princp)
        lambida = LA.eig((princp))
        cilios = lambida[0]
        
        freq1=np.zeros((4))
        dampa=np.zeros((4))

        for k in range(4):

            olho=cilios[k]
            freq1[k] = np.sqrt((olho.real)**2+(olho.imag)**2)/(2*np.pi)
            dampa[k] = (olho.real)/freq1[k]

        frequen = np.append(frequen, [[freq1[0],freq1[1],freq1[2],freq1[3]]], axis=0)
        amort = np.append(amort, [[dampa[0],dampa[1],dampa[2],dampa[3]]], axis=0)

        vel.append(V)

    y=[]
    y2=[]
    y3=[]
    y4=[]

    for i in range(len(frequen)):
        y.append(frequen[i][0])
        y2.append(frequen[i][2])
        y3.append(amort[i][0])
        y4.append(amort[i][3])


    return vel, y3,vel,y4,vel,y,vel,y2

def effcontrol(rho, a1, beta,c,eEE,Kt,E):
    e = eEE - c*0.25
    R = a1*c**2*e/Kt
    a2 = a1/np.pi*( math.acos(1-2*E)+2*np.sqrt(E*(1-E)))
    b2 = -a1/np.pi*( 1-E)*np.sqrt(E*(1-E))

    vel = []
    eff = []
    q = []

    for i in range(40):
        vel.append(i)
        q.append(0.5*1.2*i**2)
        try:
            eff.append(( 1/( (0.5*1.2*i**2)*R) + b2/(a2*e) )/( 1/((0.5*1.2*i**2)*R) -1 ))
        except:
            eff.append(1)
    
    U_rev = np.sqrt(-2*a2*e/(b2*R*rho))
    U_div = np.sqrt(2/(R*rho))
    return vel, eff, U_rev, U_div


#if __name__ == "__main__":
