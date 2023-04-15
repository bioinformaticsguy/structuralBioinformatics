import numpy as np 


file = "1fcn.pdb"


### Function Definations
def getLines(file, subString):
    lines = []
    with open(file) as pdb:
        for line in pdb:
            if line[:len(subString)] == subString:
                lines.append(line)
    return lines


def getSubstrings(listOfRows, st, en):
    subStrings = []
    for i, value in enumerate(listOfRows):
        subStrings.append((listOfRows[i][st:en]))
    return subStrings

def countOccur(value, listOfValues):
    return listOfValues.count(value)


def getPercentagess(values, uniqueValues):
    dicOfOccur = {}
    for value in uniqueValues:
        occur = countOccur(value, values)
        percentage = round(((occur/len(values))*100), 2)
        dicOfOccur[value] = percentage

    return(dicOfOccur)


## Reading the File and creating a list of rows that start with ATOM
atomLines = getLines(file, "ATOM")


### 1. Statistics (2 points):
## a) Amino acids composition (output: 3 letter code, the total number of occur-
##    rences, %) in the entire structure
print("Amino Acid composition:")
aminos = getSubstrings(atomLines, 17, 20)
uniqueAminos = set(aminos)
aminoDict = getPercentagess(aminos, uniqueAminos)
for i in aminoDict:
    print(i, aminoDict.get(i), "%")


## b) Atomic composition (statistics for Carbon, Nitrogen, Oxygen and Sulfur)
print("\nAtomic composition:")
atoms = getSubstrings(atomLines, 13, 14)
uniqueAtoms = set(atoms)

atomDict = getPercentagess(atoms, uniqueAtoms)
for i in atomDict:
    print(i, atomDict.get(i), "%")


## c) Total numbers of positively and negatively charged amino acids
posAminos = ["LYS","ARG"]
negAminos = ["ASP","GLU"]

posOccur = 0 
for posAmino in posAminos:
    posOccur += countOccur(posAmino, aminos)


negOccur = 0 
for negAmino in negAminos:    
    negOccur += countOccur(negAmino, aminos)


print("\nTotal number of positively charged residues:", posOccur)
print("Total number of negitively charged residues:", negOccur)



## 2. Count and list all the hetero atom residues in the PDB file except water (water =
## HOH in PDB format) (1 point)

# Reading the File and creating a list of rows that start with HETATM
hetroAtomLines = getLines(file, "HETATM")
hetroAtoms = getSubstrings(hetroAtomLines, 17, 20)
uniquehetroAtoms = list(set(hetroAtoms))

print(uniquehetroAtoms)
#print(uniquehetroAtoms)
##print(Since there are only LOR and HOH in the hetro atoms we are counting only LOR)

nonHOHHetroOccur = countOccur(uniquehetroAtoms[0], hetroAtoms)
print("Number of heteroatoms: ", len(uniquehetroAtoms)-1)
print(uniquehetroAtoms[0])


## 3. Distance between the two most distant residues and their residue IDs.
## Use C atoms only (2 points)
atomLines = getLines(file, "ATOM")




def getCordianteLists(atomLines):
    corDic = {}
    
    for i in atomLines:
        lastChar = i[77:78]
        if lastChar == "C":
            cor = i[32:54].split()
            cor = [float(elem) for elem in cor]
            resID = i[8:12] 
            corDic[resID] = cor
    return corDic



def calEucDist(a, b):
    a = np.array(a)
    b = np.array(b)
    s = np.sum(np.square(a - b))
    return np.sqrt(s)
        
    






