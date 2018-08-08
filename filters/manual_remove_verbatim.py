
''' 
Manual filter to remove \begin{verbatim}\end{verbatim} while converting MD
file extracted from jupyter-notebook into a latex file. This allows to have
the proper synthax for input/output cells.

WARNING:
  This depends on template/nbconverter_md_pandoc.tpl 
  and template/document_template.tex
'''



def find_first_sublist(seq, sublist, start=0):
    length = len(sublist)
    for index in range(start, len(seq)):
        if seq[index:index+length] == sublist:
            return index, index+length

def replace_sublist(seq, sublist, replacement):
    length = len(replacement)
    index = 0
    for start, end in iter(lambda: find_first_sublist(seq, sublist, index), None):
        seq[start:end] = replacement
        index = start + length
        
find = [
    ['\\begin{input_code}\n', '\n', '\\begin{verbatim}\n'],
    ['\\end{verbatim}\n', '\n', '\\end{input_code}\n'],
    ['\\begin{output_code}\n', '\n', '\\begin{verbatim}\n'],
    ['\\end{verbatim}\n', '\n', '\\end{output_code}\n'],
    ['\\begin{input_code}\n', '\n', '\\begin{lstlisting}\n'],
    ['\\end{lstlisting}\n', '\n', '\\end{input_code}\n'],
    ['\\begin{output_code}\n', '\n', '\\begin{lstlisting}\n'],
    ['\\end{lstlisting}\n', '\n', '\\end{output_code}\n'],
]

replace = [
    ['\\begin{input_code}\n'],
    ['\\end{input_code}\n'],
    ['\\begin{output_code}\n'],
    ['\\end{output_code}\n'],
    ['\\begin{input_code}\n'],
    ['\\end{input_code}\n'],
    ['\\begin{output_code}\n'],
    ['\\end{output_code}\n'],
]


import argparse

parser = argparse.ArgumentParser(description='Manual removal of verbatim environment')
parser.add_argument('-i', type=str, help='input tex file')
parser.add_argument('-o', type=str, help='output tex file')
args = parser.parse_args()

with open(args.i,'r') as infile:
    lines = [l for l in infile]
    for f,r in zip(find,replace):
        replace_sublist(lines,f,r)
    outfile = open(args.o,'w')
    for l in lines:
        outfile.write(l)


