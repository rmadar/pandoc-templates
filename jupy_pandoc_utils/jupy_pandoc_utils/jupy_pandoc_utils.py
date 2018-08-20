
import os
from IPython.display import Markdown
from tabulate import tabulate

jupy_pandoc_COUNTERS={}

def plt2md(figname,figcaption='figure',figsize=None,figlabel=None):
    '''
    Doc string to be written
    '''
    import matplotlib.pyplot as plt
    global jupy_pandoc_COUNTER

    if figname not in jupy_pandoc_COUNTERS:
        jupy_pandoc_COUNTERS[figname]=0
        
    for i in range(0,jupy_pandoc_COUNTERS[figname]):
        oldfilename=os.path.join(os.getcwd(),figname+'__n'+str(i)+'.png')
        if (os.path.isfile(oldfilename)):
            os.remove(oldfilename)
            
    figname_tmp = figname+'__jpu_n'+str(jupy_pandoc_COUNTERS[figname])+'.png'
    plt.savefig(figname_tmp)
    plt.savefig(figname+'.pdf')
    plt.savefig(figname+'.png')
    plt.close()
    strMD='![{}]({})'.format(figcaption,figname_tmp)
    if figsize and figlabel:
        strMD+='{' + 'width={} #'.format(figsize) + figlabel + '}'
    elif figsize:
        strMD+='{' + 'width={}'.format(figsize)+'}'
    elif figlabel:
        strMD+='{ #'+ figlabel + '}'

    jupy_pandoc_COUNTERS[figname]+=1
    return display(Markdown(strMD))


def df2md(df,caption=None,label=None):
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
    output += '\n'
    if caption:
        output += 'Table: ' + caption
    if label:
        output += ' {'+label+'}'
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
    os.rename(name.replace('.ipynb','_clean.ipynb'),name)


def nb2md(name,png2pdf=True):
    '''
    Doc string to be written soon
    '''
    os.system('jupyter-nbconvert --to markdown ' + name +
              ' --template=${PANDOC_TEMPLATES}/nbconverter_md_pandoc.tpl')
    outname=name.replace('.ipynb','.md')
    fin=open(outname,'r')
    fout=open(outname.replace('.md','_clean.md'),'w')

    # list of figure in current directories
    import glob
    import sys
    isPython3 = sys.version_info[0] > 3
    pngfile_list,pdffile_list=[],[]
    if isPython3:
        pngfile_list=glob.glob('**/*.png',recursive=True)
        pdffile_list=glob.glob('**/*.pdf',recursive=True)
    else:
        for dirpath, dirs, files in os.walk("."):
	    for f in files:
                if f.endswith('.png'): pngfile_list.append(os.path.join(dirpath,f).replace('./',''))
                if f.endswith('.pdf'): pdffile_list.append(os.path.join(dirpath,f).replace('./',''))
        
    # Replace png by pdf
    for l in fin:
        for s in pngfile_list:
            if s in l and s.replace('.png','.pdf') in pdffile_list and png2pdf:
                l=l.replace(s,s.replace('.png','.pdf'))
        fout.write(l)
    fin.close()
    fout.close()


    if png2pdf:
        finalfile=outname.replace('.md','_pdf.md')
    else:
        finalfile=outname.replace('.md','_png.md')
        
    os.rename(outname.replace('.md','_clean.md'),finalfile)
    print(finalfile + ' is created')
    return
