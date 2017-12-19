#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Jiang Yida"
__pkuid__  = "1700011739"
__email__  = "1700011739@pku.edu.cn"
"""

import sys
from urllib.request import urlopen



def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    counts = {}#set dietionary

    #split
    text=lines.split()
    for i in ''' ,.:"';[]()?!-_*#''':
        l1=[]
        for i1 in text:
            l1.extend(i1.split(i))
        text=[]
        text=l1[:]

    #count
    for l in text:
        counts[l] = counts.get(l, 0) + 1

    #compare and print
    l1=[]
    l2=[]

    for i in counts:
        l1.append(i)
        l2.append(counts[i])
    if '' in l1:#del ''
        del l2[l1.index('')]
        del l1[l1.index('')]
    for i in range(topn):#print
        print('%-15s%d'%(l1[l2.index(max(l2))],max(l2)))
        del l1[l2.index(max(l2))]
        del l2[l2.index(max(l2))]
        
    

if __name__ == '__main__':


    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
 
