
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
        
    for i in range(0,jupy_pandoc_COUNTERS[figlabel]):
        oldfilename=os.path.join(os.getcwd(),figlabel+'__n'+str(i)+'.png')
        if (os.path.isfile(oldfilename)):
            os.remove(oldfilename)
            
    figname = figlabel+'__jpu_n'+str(jupy_pandoc_COUNTERS[figlabel])+'.png'
    plt.savefig(figname)
    plt.savefig(figlabel+'.pdf')
    plt.savefig(figlabel+'.png')
    plt.close()
    strMD='![{}]({})'.format(figcaption,figname) \
        +'{' + 'width={} #'.format(figsize) + figlabel + '}'

    jupy_pandoc_COUNTERS[figlabel]+=1
    return display(Markdown(strMD))


def df2md(df,caption=None):
    '''
    Docd string to be written soon
    '''
    import copy
    df2 = copy.copy(df)
    df2['labels'] = ['**'+str(i)+'**' for i in df.index]
    rename_dict = {str(k):'**'+str(k)+'**' for k in df2.keys()}
    df3=df2.rename(index=str, columns=rename_dict)
    c=df3.columns.tolist()
    c=c[-1:]+c[:-1]
    df3=df3[c]
    output = tabulate(df3, headers='keys',tablefmt='pipe',showindex=False)
    if caption:
        output += '\n'
        output += 'Table: ' + caption
    return display(Markdown(output))


def clean_notebook(name):
    '''
    Doc string to be written
    '''
    find = ['__jpu_n'+str(i) for i in range(0,1000)]
    fin=open(name,'r')
    fout=open(name.replace('.ipynb','_clean.ipynb'),'w')
    for l in fin:
        for s in find:
            if s in l:
                l=l.replace(s,'')
        fout.write(l)
    fin.close()
    fout.close()
