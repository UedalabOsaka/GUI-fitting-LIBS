def plot_ini():
    import matplotlib.pyplot as plt
    plt.rcParams['font.family'] ='sans-serif'#使用するフォント
    plt.rcParams['xtick.direction'] = 'in'#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = 'in'#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['xtick.major.width'] = 2.0#x軸主目盛り線の線幅
    plt.rcParams['ytick.major.width'] = 2.0#y軸主目盛り線の線幅
    plt.rcParams['xtick.minor.width'] = 2.0#x軸副目盛り線の線幅
    plt.rcParams['ytick.minor.width'] = 2.0#y軸副目盛り線の線幅
    plt.rcParams['font.size'] = 16 #フォントの大きさ
    plt.rcParams['axes.linewidth'] = 2.0# 軸の線幅edge linewidth。囲みの太さ
    
    #plt.figure(figsize=(8,8))
    #plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))#軸の数字が整数になるようにする
    #plt.locator_params(axis='y',nbins=6)#y軸，6個以内．
    return

def plotset():
    import matplotlib.pyplot as plt
    plt.legend()
    plt.minorticks_on()
    plt.tick_params(axis='both',which='both', top=True, right=True)
    plt.tight_layout()
    
    return