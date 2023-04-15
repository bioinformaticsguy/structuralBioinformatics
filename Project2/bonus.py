import matplotlib.pyplot as plt
import sys
from sys import exit

### Get file name from the sys argument
file = sys.argv[1]

### Function Definations
def getLines(file, subString):
    lines = []
    with open(file) as pdb:
        for line in pdb:
            if line[:len(subString)] == subString:
                lines.append(line)
    return lines


def getAminos(atomLines):
    aminos = []
    for i in atomLines:
        line = (i[19:].split())
        for amino in line:
            aminos.append(amino)
    return aminos


def getKyteScaleDict():
    protScale = {
    "Ala" :  1.800,  
    "Arg" : -4.500,  
    "Asn" : -3.500,  
    "Asp" : -3.500,  
    "Cys" :  2.500,  
    "Gln" : -3.500,  
    "Glu" : -3.500,  
    "Gly" : -0.400,  
    "His" : -3.200,  
    "Ile" :  4.500,  
    "Leu" :  3.800,  
    "Lys" : -3.900,
    "Met" :  1.900,  
    "Phe" :  2.800,  
    "Pro" : -1.600,  
    "Ser" : -0.800,  
    "Thr" : -0.700,  
    "Trp" : -0.900,  
    "Tyr" : -1.300,  
    "Val" :  4.200
    }

    return protScale



def mapToKyte(aminoList):
    mappedList = []
    protScale = getKyteScaleDict()

    for i in aminoList:
        val = protScale.get(i.capitalize())
        mappedList.append(val)
    return mappedList

def getAverage(listOfValues):
    return sum(listOfValues)/len(listOfValues)


def smoothIt(mapedList, windowSize = 3):
    windowSize = int(windowSize)
    if (windowSize % 2) == 0:
        print("Window parameter should be an odd number \n Exiting!")
        exit()

    averages = []
    for i in range(len(mapedList)-(1+windowSize)):
        tempValues = mapedList[i:windowSize+i]
        average = getAverage(tempValues)
        averages.append(average)
    return averages        
        



## Reading the File and creating a list of rows that start with ATOM
SEQRESLines = getLines(file, "SEQRES")
aminoList = getAminos(SEQRESLines)
mapedList = mapToKyte(aminoList)
aveValues = smoothIt(mapedList, sys.argv[2])


## Creating Line Graph   
xAxis = [i for i in range(1, len(aveValues)+1)]
yAxis = aveValues
plt.plot(xAxis, yAxis)
plt.title('Hydrophobicity Graph of protein: ' + file[:-4])
plt.xlabel('Number of Residues')
plt.ylabel('Hydrophobicity')
plt.show()

## Saving the file
plt.savefig(file[:-4] + "_GraHyphob.png")
