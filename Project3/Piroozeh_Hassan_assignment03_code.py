from pprint import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logomaker as lm
import sys
from Bio import AlignIO
from Bio.Align import AlignInfo


## Get File Names
fileName = sys.argv[1]


## Function Definations
def getLines(fileName):
    lol = []
    with open(fileName) as f:   
        for i in f:
            lol.append(i)
    
    return lol

def getAlignmentChunks(lol):
    chunks = []
    temp = []
    for i in range(3, len(lol)):
        if len(lol[i]) > 1:
            if lol[i][1] != " ":
                temp.append(lol[i])
        if len(lol[i]) == 1:
            chunks.append(temp)
            temp = []
    return chunks

def getListOfBases(chunk, i):
    return [alignment[i] for  alignment in chunk] 


def getAlignProteinStrings(chunks):
    joinedChunk = []
    for i in range(len(chunks[0])):
        align = ""  
        for chunk in chunks:
            align = align + chunk[i][14:74]
        joinedChunk.append(align)
    return joinedChunk

def stripChunks(chunks):
    strippedChunks = []
    for chunk in chunks:
        strippedChunk = []
        for align in chunk:
            strippedChunk.append(align[14:74])
        strippedChunks.append(strippedChunk)
    return strippedChunks
    


## Task 3 consensus sequence
align = AlignIO.read(fileName, "clustal")
summary_align = AlignInfo.SummaryInfo(align)
consensus = summary_align.dumb_consensus()
print("Here is consensus sequence for your file:\n", fileName, "\n")
print(consensus)



## Task 4 Sequence Profiles to a CSV file.
chunks = getAlignmentChunks(getLines(fileName))
seqs = getAlignProteinStrings(chunks)
seqsDF = lm.alignment_to_matrix(sequences=seqs, to_type='counts', characters_to_ignore='.-X')
seqsDF.to_csv("sequenceProfile.csv", index = True, header=True)


## Sequence logos (Bonus Point)
chunks = stripChunks(chunks)

print(chunks)

for i, chunk in enumerate(chunks):
    chunkSeqProfile = lm.alignment_to_matrix(chunk)
    lm.Logo(chunkSeqProfile)
    figureName = 'sequenceLogo_' + str(i) + '.png'
    plt.savefig(figureName)





##from Bio import SeqIO
##from Bio.Seq import Seq
##from Bio.Align import AlignInfo
##
##import logomaker
##
####a = SeqIO.parse(file, "fasta")
##
##
##summary_align = AlignInfo.SummaryInfo(align)
##
####print(summary_align)
####
####print(len(summary_align.dumb_consensus()))
##
####consensus = summary_align.dumb_consensus(a)
##
##
##
####b = motifs.create(instances)
##
####print(a)
##
####logomaker.demo('fig1b')
##
##import logomaker as lm
##
##
##

##seqs = [ 'ATAAGCAGGATTTAGCTCACACTAAT',
##         'AAAAATGTGATACCAATCACAGAATA',
##         'ATATTGGTGATCCATAAAACAATATT',
##         'ATATTGGTGAGGAACTTAACAATATT',
##         'GAATATTTGCACGGCGTCACACTTTT']
##
##
##seqs = [ 'TTAAGC',
##         'AAAAAC',
##         'CTATTC',
##         'ATATTC',
##         'ATATTC',
##         'GAATAC']
##
##counts_mat = lm.alignment_to_matrix(seqs)
####
##print(counts_mat)
##
##
##lm.Logo(counts_mat)
##
##plt.show()




##seqs = ['LPPQW..TEA.VDVDT...GKFYFVHVET.......KETRWERP',
##        '--PGW..TAT.VDPAS...GRTYYYHAAT.......GETRWEPP',
##        'LPSGW..VEQ.TDPSS...GRPYYYHNAS.......NLTQWERP',
##        'LPAGW..VAA.NDPSS...GRTYYYHAES.......GVTSWNPP',
##        'LPNGW..QEL.VDPSS...GSTYYYNEVN.......GTTSWDRP',
##        'LPEGW..VEL.VHESS...GKTYYFHAED.......NVTSWEQP',
##        'LPQGW..IEA.VDPST...EATYYINEVE.......GITSWERP',
##        'LPPGW..AKL.THPDS...GDAYYYNEAT.......NATSWDIP',
##        '--TGW..EAL.VDEAS...GAIYYYNKLD.......GTSSWERP',
##        'LPEGW..IEV.MDPNS...GSVYYFNEVD.......GTSSWDKP']
##
##
##seqs = getAlignProteinStrings(chunks)
##
##ww_counts_df = lm.alignment_to_matrix(sequences=seqs, to_type='counts', characters_to_ignore='.-X')
##pprint(ww_counts_df.head())
##
##
##
##
##import pandas as pd
##print(type(ww_counts_df))
##print(pd.DataFrame(ww_counts_df))
##
##
##ww_counts_df.to_csv("sequenceProfile.csv", index = True, header=True)


##lm.Logo(ww_counts_df)
##
##plt.show()
























