import os
import numpy as np
import scipy as sp
import scipy.optimize as opt
import math as math
import matplotlib.pyplot as plt
import itertools as IT
from scipy import integrate
from scipy.integrate import simps
###IMPORT ORIGINAL FUNCTIONS##################################################
from func000_Plotset import plot_ini
from func000_Plotset import plotset
plot_ini()
##############################################################################

def norm(x, mean, sd):
    norm = []
    for i in range(x.size):
        norm += [1.0/(sd*np.sqrt(2*np.pi))*np.exp(-(x[i] - mean)**2/(2*sd**2))]
    return np.array(norm)

def peakfind(x_peak,x_min,x_max,nx,XX,YY,k):
    del_x=0.0
    x_peakD=x_peak
    j=0
    while XX[j] < x_min:
        jmin=j
        j+=1
    j=jmin
    preYY=YY[j]
    while XX[j] < x_max:
        j+=1
        if YY[j]>preYY:
            x_peakD=XX[j]
        preYY=YY[j]
        
    del_x=x_peakD-x_peak
    #print("del_x",del_x)
    return del_x

def peakfit(x_peak,x_min,x_max,nx,XX,YY,sd1,a1,k,flg):
    m1 = x_peak
    j=0
    while XX[j] < x_min:
        jmin=j-2
        j+=1
    while XX[j] < x_max:
        jmax=j+2
        j+=1
    jlen=jmax-jmin
    #print("jmin={0:},jmax={1:}".format(jmin,jmax))
    #print("XX(jmin)={0:},XX(jmax)={1:}".format(XX[jmin],XX[jmax]))
    XXX=XX[jmin:jmax]
    YYY=YY[jmin:jmax]

    x = np.arange(x_min, x_max, (x_max-x_min)/nx)


############################################################################
    # Solving

    BG=YY[jmin]
    BGa=3.0e2
    p = [m1, sd1,a1,BGa,BG] # Initial guesses for leastsq
    y_init = a1*norm(x, m1, sd1)+BGa*x+BG # For final comparison plot
    y_init=y_init

    def res(p, y, x):
      m1, sd1, a1,  BGa, BG = p
      m1 = m1
      y_fit = a1*norm(x, m1, sd1) + BGa*x + BG
      err = y - y_fit
      return err

    plsq = opt.leastsq(res, p, args = (YYY,XXX))
############################################################################
    m1,sd1 = plsq[0][0], plsq[0][1]
    BGa,BG = plsq[0][3],plsq[0][4]
    y_fit=plsq[0][2]*norm(x, m1, sd1)
    y_data=YYY-(XXX*BGa+BG)
    y1_est= y_fit+BGa*x+BG
    #eqsum=np.sum(plsq[0][2]*norm(x, plsq[0][0], plsq[0][1]))
    #eqint=simps(y_data, XXX)
    eqint=simps(y_fit,x)

    if flg==1:
        prt1='m1={0:.2f} '.format(m1)
        prt2='sd1={0:.2f} '.format(sd1)
        prt3='a1={0:.2e} '.format(plsq[0][2])
        prt4='BG={0:.3e}x{1:+.3e} '.format(BGa,BG)
        prt5='eqint={0:.2e} '.format(eqint)
        prt=[prt1,prt2,prt3,prt4,prt5]
        print("Spectral-fit #{} is DONE".format(k))
        print(prt)
        
        plt.title(prt1+prt2+"\n"+prt3+prt4+"\n"+prt5,fontsize=8)
        plt.plot(XXX, YYY, 'ro',label='Real Data')
        plt.plot(x, y_init, 'b-',lw=1, label='Starting Guess')
        plt.plot(x, y1_est, 'g-',lw=3, label='y1_Fitted')
        plt.plot(x, BGa*x+BG, 'm-',lw=1, label='Background')
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Intensity (a.u.)')
        plt.xlim(x_min,x_max);
        plt.ylim(0,1.e4);
        plotset()
        plt.legend(fontsize=12)
        plt.savefig("4-3_Spectral-fit{}.png".format(k),format = 'png', dpi=300)
        
        #plt.show()    
        plt.close()

    return eqint, m1, sd1