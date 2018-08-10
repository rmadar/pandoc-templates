
from IPython.display import Markdown
from tabulate import tabulate

jupy_pandoc_COUNTER=0

def plt2md(figlabel,figcaption,figsize):
    global jupy_pandoc_COUNTER
    figname = figlabel+'_'+str(jupy_pandoc_COUNTER)+'.png'
    plt.tight_layout()
    plt.savefig(figname)
    plt.savefig(figlabel+'.pdf')
    strMD='![{}]({})'.format(figcaption,figname) +\
        '{' + 'width={} #'.format(figsize) + figlabel + '}'
    jupy_pandoc_COUNTER+=1
    return display(Markdown(strMD))


def df2md(df):
    return display(
        Markdown(
            tabulate(df, headers='keys',tablefmt='pipe')
        )
    )
