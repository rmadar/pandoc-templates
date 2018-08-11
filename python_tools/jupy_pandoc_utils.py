
import os
from IPython.display import Markdown
from tabulate import tabulate

jupy_pandoc_COUNTERS={}

def plt2md(figlabel,figcaption,figsize):
    '''
    Doc string to be written
    '''
    import matplotlib.pyplot as plt
    global jupy_pandoc_COUNTER

    if figlabel not in jupy_pandoc_COUNTERS:
        jupy_pandoc_COUNTERS[figlabel]=0
        
    # Incrementation is needed to see the updated file in jupyter
    # due to data caching in web browser. To avoid a large amount
    # of png, the last one only is kept.
    for i in range(0,jupy_pandoc_COUNTERS[figlabel]):
        oldfilename=os.path.join(os.getcwd(),figlabel+'__n'+str(i)+'.png')
        if (os.path.isfile(oldfilename)):
            os.remove(oldfilename)
            
    figname = figlabel+'__n'+str(jupy_pandoc_COUNTERS[figlabel])+'.png'
    plt.savefig(figname)
    plt.savefig(figlabel+'.pdf')
    plt.close()
    strMD='![{}]({})'.format(figcaption,figname) \
        +'{' + 'width={} #'.format(figsize) + figlabel + '}'

    jupy_pandoc_COUNTERS[figlabel]+=1
    return display(Markdown(strMD))


def df2md(df):
    '''
    Doc string to be written
    '''
    return display( Markdown(tabulate(df, headers='keys',tablefmt='pipe') ))
