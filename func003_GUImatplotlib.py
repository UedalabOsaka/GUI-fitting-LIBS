# -*- coding: utf-8 -*-
def gui2():
    #%matplotlib qt
    from matplotlib import interactive
    interactive(True)
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider, Button, RadioButtons
    fig= plt.figure(figsize=(3,3))
    #plt.subplots_adjust(left=0., bottom=0.1, right=0.48)
    flg=0
    def NO(evt):
        flg=0
        print('previous data NOT used!')


    def OK(event):         
        flg=1
        print('previous data IS used!')
        
    axcolor = 'lightgoldenrodyellow'
    notax = plt.axes([0.55, 0.5, 0.4, 0.3])
    button2 = Button(notax, 'No, thanks', color=axcolor, hovercolor='0.975')
    button2.on_clicked(NO)
    
    oktax = plt.axes([0.05, 0.5, 0.4, 0.3])
    OKbutton = Button(oktax, 'OK', color=axcolor, hovercolor='0.975')
    OKbutton.on_clicked(OK)
    
    
    plt.show(block=True)
    
    plt.close()
    return flg

def gui(x,y,m,sd,a,BG,n):
    #%matplotlib qt
    from matplotlib import interactive
    interactive(True)
    
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider, Button, RadioButtons

    
    fig, ax = plt.subplots(1,1, figsize=(15,9))# figure内の枠の大きさとどこに配置しているか。subplot(行の数,列の数,何番目に配置しているか)
#    plt.rcParams["figure.figsize"] = [16, 8]
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.48)
    #plt.subplots_adjust(left=0.25, bottom=0.25)
    #t = np.arange(0.0, 1.0, 0.001)
    nx=500
    xf=np.arange(np.min(x),np.max(x),(np.max(x)-np.min(x))/nx)
    
    def axb(x1,x2,y1,y2): #y=ax+b
        a=(y2-y1)/(x2-x1)
        b=y1-a*x1
        return a,b
    
    jlen=len(x)
    y1N=BG[0]*x[0]+BG[1]
    y2N=BG[0]*x[jlen-1]+BG[1]
    #BG[0],BG[1]=axb(x[0],x[jlen-1],y1N,y2N)
                
    def norm(xf, mean, sd):
      norm = []
      for i in range(xf.size):
        norm += [1.0/(sd*np.sqrt(2*np.pi))*np.exp(-(xf[i] - mean)**2/(2*sd**2))]
      return np.array(norm)
    
    def line(xf,a,m,sd,BG):
        k=0
        y_init=0.0
        while k < n:
            y_init += a[k]*norm(xf,m[k],sd[k])
            k +=1 
        
        y_init +=BG[0]*xf+BG[1]
        return y_init
    
    y_init=line(xf,a,m,sd,BG)
    plt.xlabel('Wavelengh(nm)')
    plt.ylabel('Intensity')
    k, = plt.plot(x, y, 'o', color='red')
    l, = plt.plot(xf, y_init, lw=2, color='blue')
    yBG=BG[0]*xf+BG[1]
    lBG, = plt.plot(xf, yBG, lw=2)
    
    y1 = a[0]*norm(xf,m[0],sd[0])+yBG
    l1, = plt.plot(xf, y1, lw=2)
    if n>1:
        y2 = a[1]*norm(xf,m[1],sd[1])+yBG
        l2, = plt.plot(xf, y2, lw=2)
    if n>2:
        y3 = a[2]*norm(xf,m[2],sd[2])+yBG
        l3, = plt.plot(xf, y3, lw=2)
    if n>3:
        y4 = a[3]*norm(xf,m[3],sd[3])+yBG
        l4, = plt.plot(xf, y4, lw=2)
    if n>4:
        y5 = a[4]*norm(xf,m[4],sd[4])+yBG
        l5, = plt.plot(xf, y5, lw=2)    
        
    plt.axis([np.min(x), np.max(x), 0.0, np.max(y)*1.2])
    
    
# Sliderの位置設定   
        

    #print(i,np.size(ax1))
    axcolor = 'lightgoldenrodyellow'
    kx=0.57
    kaxes1=0.92
    kaxes2=0.77
    kaxes3=0.62
    kaxes4=0.47
    kaxes5=0.32
    kaxesBG=0.18
    plt.text(kx, kaxes1, 'Signal[1]', transform=fig.transFigure)
    ax1 = plt.axes([kx, kaxes1-0.07, 0.2, 0.03], facecolor=axcolor)
    ax2 = plt.axes([kx, kaxes1-0.04, 0.2, 0.03], facecolor=axcolor)
    ax3 = plt.axes([kx, kaxes1-0.10, 0.2, 0.03], facecolor=axcolor)
    
    if n>1:
        plt.text(kx,kaxes2, 'Signal[2]', transform=fig.transFigure)
        ax4 = plt.axes([kx, kaxes2-0.07, 0.2, 0.03], facecolor=axcolor)
        ax5 = plt.axes([kx, kaxes2-0.04, 0.2, 0.03], facecolor=axcolor)
        ax6 = plt.axes([kx, kaxes2-0.10, 0.2, 0.03], facecolor=axcolor)

    if n>2:
        plt.text(kx,kaxes3, 'Signal[3]', transform=fig.transFigure)
        ax7 = plt.axes([kx, kaxes3-0.07, 0.2, 0.03], facecolor=axcolor)
        ax8 = plt.axes([kx, kaxes3-0.04, 0.2, 0.03], facecolor=axcolor)
        ax9 = plt.axes([kx, kaxes3-0.1, 0.2, 0.03], facecolor=axcolor)
    if n>3:
        plt.text(kx, kaxes4, 'Signal[4]', transform=fig.transFigure)
        ax10 = plt.axes([kx, kaxes4-0.07, 0.2, 0.03], facecolor=axcolor)
        ax11 = plt.axes([kx, kaxes4-0.04, 0.2, 0.03], facecolor=axcolor)
        ax12 = plt.axes([kx, kaxes4-0.1, 0.2, 0.03], facecolor=axcolor)
    if n>3:
        plt.text(kx, kaxes5, 'Signal[5]', transform=fig.transFigure)
        ax13 = plt.axes([kx, kaxes5-0.07, 0.2, 0.03], facecolor=axcolor)
        ax14 = plt.axes([kx, kaxes5-0.04, 0.2, 0.03], facecolor=axcolor)
        ax15 = plt.axes([kx, kaxes5-0.1, 0.2, 0.03], facecolor=axcolor)
        
    plt.text(kx, kaxesBG, 'BG', transform=fig.transFigure)
    axBG0 = plt.axes([kx, kaxesBG-0.07, 0.2, 0.03], facecolor=axcolor)
    axBG1 = plt.axes([kx, kaxesBG-0.04, 0.2, 0.03], facecolor=axcolor)
    Namp=4
    Nsd=4
    samp = Slider(ax1, 'Amp', a[0]*0, a[0]*Namp, valinit=a[0],valfmt='%1.2e')
    sposi = Slider(ax2, 'Posi', np.min(x), np.max(x), valinit=m[0])
    ssd = Slider(ax3, 'SD', sd[0]*0, sd[0]*Nsd, valinit=sd[0])

    if n>1:
        samp2 = Slider(ax4, 'Amp', a[1]*0, a[1]*Namp, valinit=a[1],valfmt='%1.2e')
        sposi2 = Slider(ax5, 'Posi', np.min(x), np.max(x), valinit=m[1])
        ssd2 = Slider(ax6, 'SD', sd[1]*0, sd[1]*Nsd, valinit=sd[1])    
    if n>2:
        samp3 = Slider(ax7, 'Amp', a[2]*0, a[2]*Namp, valinit=a[2],valfmt='%1.2e')
        sposi3 = Slider(ax8, 'Posi', np.min(x), np.max(x), valinit=m[2])
        ssd3 = Slider(ax9, 'SD', sd[2]*0, sd[2]*Nsd, valinit=sd[2])  
    if n>3:
        samp4 = Slider(ax10, 'Amp', a[3]*0, a[3]*Namp, valinit=a[3],valfmt='%1.2e')
        sposi4 = Slider(ax11, 'Posi', np.min(x), np.max(x), valinit=m[3])
        ssd4 = Slider(ax12, 'SD', sd[3]*0, sd[3]*Nsd, valinit=sd[3])          
    if n>4:
        samp5 = Slider(ax13, 'Amp', a[4]*0, a[4]*Namp, valinit=a[4],valfmt='%1.2e')
        sposi5 = Slider(ax14, 'Posi', np.min(x), np.max(x), valinit=m[4])
        ssd5 = Slider(ax15, 'SD', sd[4]*0, sd[4]*Nsd, valinit=sd[4]) 
        
    BG0=np.sign(y2N)*0.8
    BG1=np.sign(y1N)*0.8
    sBG0 = Slider(axBG0, 'BG right', (y2N)*(1-BG0), (y2N)*(1+BG0), valinit=y2N,valfmt='%1.2e')
    sBG1 = Slider(axBG1, 'BG left',(y1N)*(1-BG0), (y1N)*(1+BG0), valinit=y1N,valfmt='%1.2e')
    
    #t1p = plt.axes([0.85, 0.2, 0.1, 0.04])
    #t2p = plt.axes([0.85, 0.1, 0.1, 0.04])
    
#    button2 = Button(resetax, 'Set', color=axcolor, hovercolor='0.975')
    t1 = fig.text(0.87,kaxesBG-0.03, "BG0={:1.2e}".format(BG[0]))
    t2 = fig.text(0.87,kaxesBG-0.06, "BG1={:1.2e}".format(BG[1]))
    
        
        
    def update(val):
        
        y2N=sBG0.val
        y1N=sBG1.val
        
        BG[0],BG[1]=axb(x[0],x[jlen-1],y1N,y2N)
        
        yBG=BG[0]*xf+BG[1]
        lBG.set_ydata(yBG)
        #print(y[0],y2N,BG)
    
        a[0]= samp.val
        m[0] = sposi.val
        sd[0] = ssd.val
        y1 = a[0]*norm(xf,m[0],sd[0])+yBG
        l1.set_ydata(y1)
        if n>1:
            a[1]= samp2.val
            m[1] = sposi2.val
            sd[1] = ssd2.val
            y2 = a[1]*norm(xf,m[1],sd[1])+yBG
            l2.set_ydata(y2)
        if n>2:
            a[2]= samp3.val
            m[2] = sposi3.val
            sd[2] = ssd3.val
            y3 = a[2]*norm(xf,m[2],sd[2])+yBG
            l3.set_ydata(y3)
        if n>3:
            a[3]= samp4.val
            m[3] = sposi4.val
            sd[3] = ssd4.val
            y4 = a[3]*norm(xf,m[3],sd[3])+yBG
            l4.set_ydata(y4)
        if n>3:
            a[4]= samp5.val
            m[4] = sposi5.val
            sd[4] = ssd5.val
            y5 = a[4]*norm(xf,m[4],sd[4])+yBG
            l5.set_ydata(y5)
        y_up=line(xf,a,m,sd,BG)
        l.set_ydata(y_up)
        t1.set_text("BG0={:1.3e}".format(BG[0]))
        t2.set_text("BG1={:1.3e}".format(BG[1]))
        fig.canvas.draw_idle()
    
        
    def updateBG0(val):
        y1N=BG[0]*x[0]+BG[1]
        y2N=sBG0.val
        BG[0],BG[1]=axb(x[0],x[jlen-1],y1N,y2N)
        
    def updateBG1(val):
        #BG[1]=BG[1]-sBG1.val
        y1N=BG[0]*x[0]+BG[1]+sBG1.val
        y2N=sBG0.val+sBG1.val
        BG[0],BG[1]=axb(x[0],x[jlen-1],y1N,y2N)
        
        

    #sBG0.on_changed(updateBG0)
    #sBG1.on_changed(updateBG1)
    sBG0.on_changed(update)
    sBG1.on_changed(update)
    samp.on_changed(update)
    sposi.on_changed(update)
    ssd.on_changed(update)
    if n>1:
        samp2.on_changed(update)
        sposi2.on_changed(update)
        ssd2.on_changed(update)
    if n>2:
        samp3.on_changed(update)
        sposi3.on_changed(update)
        ssd3.on_changed(update)    
    if n>3:
        samp4.on_changed(update)
        sposi4.on_changed(update)
        ssd4.on_changed(update)         
    if n>4:
        samp5.on_changed(update)
        sposi5.on_changed(update)
        ssd5.on_changed(update)    
        
    resetax = plt.axes([0.7, 0.05, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


    def reset(event):
        sBG0.reset()
        sBG1.reset()
        samp.reset()
        sposi.reset()
        ssd.reset()
        if n>1:
            samp2.reset()
            sposi2.reset()
            ssd2.reset()
        if n>2:
            samp3.reset()
            sposi3.reset()
            ssd3.reset()
        if n>3:
            samp4.reset()
            sposi4.reset()
            ssd4.reset()    
        if n>4:
            samp5.reset()
            sposi5.reset()
            ssd5.reset()  
            
    button.on_clicked(reset)
    
    def handle_close(evt):
        print('Closed Figure!')
        plt.close()
    
    resetax = plt.axes([0.85, 0.05, 0.1, 0.04])
    button2 = Button(resetax, 'Set', color=axcolor, hovercolor='0.975')
    button2.on_clicked(handle_close)


    
    plt.show(block=True)
    
    return x,y,m,sd,a,BG,n

"""
    color button
    rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
    radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)

    def colorfunc(label):
        k.set_color(label)
        fig.canvas.draw_idle()
    radio.on_clicked(colorfunc)
"""
    
    