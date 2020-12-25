integerMass = {"G": 57,\
"A": 71,\
"S": 87,\
"P": 97,\
"V": 99,\
"T": 101,\
"C": 103,\
"I": 113,\
"L": 113,\
"N": 114,\
"D": 115,\
"K": 128,\
"Q": 128,\
"E": 129,\
"M": 131,\
"H": 137,\
"F": 147,\
"R": 156,\
"Y": 163,\
"W": 186}

def expand(candidatePeptides):
    newCandidatePeptides = []
    avaAminos = list(integerMass.keys())
    for pep in candidatePeptides:
        for am in avaAminos:
            newPep = pep + am
            newCandidatePeptides.append(newPep)
    return newCandidatePeptides

def getWeight(aminoSubPep):
    weight = 0
    for am in aminoSubPep:
        weight += integerMass[am]
    return weight

def generateSubpeptidesCyclic(aminoPep):
    subpeptides = []
    for i in range(1, len(aminoPep)):
        tempAminoPep = aminoPep+aminoPep[0:i]
        for j in range(0, len(tempAminoPep)-i):
            subpep = tempAminoPep[j:j+i]
            subpeptides.append(subpep)
    subpeptides.append(aminoPep)
    return subpeptides

def generateSubpeptidesLinear(aminoPep):
    subpeptides = []
    for i in range(1, len(aminoPep)):
        tempAminoPep = aminoPep
        for j in range(0, len(tempAminoPep)-i+1):
            subpep = tempAminoPep[j:j+i]
            subpeptides.append(subpep)
    subpeptides.append(aminoPep)
    return subpeptides
    
def cycloSpectrum(aminoPep):
    subpeptides = generateSubpeptidesCyclic(aminoPep)
    spectrum = [0]
    for subpep in subpeptides:
        spectrum.append(getWeight(subpep))
    spectrum = list(map(int, spectrum))
    spectrum.sort()
    spectrum = list(map(str, spectrum))
    return spectrum

def linearSpectrum(aminoPep):
    subpeptides = generateSubpeptidesLinear(aminoPep)
    spectrum = [0]
    for subpep in subpeptides:
        spectrum.append(getWeight(subpep))
    spectrum = list(map(int, spectrum))
    spectrum.sort()
    spectrum = list(map(str, spectrum))
    return spectrum

def isConsistent(theoCycloSpec, spectrum):
    consistent = True
    s = spectrum.copy()
    for val in theoCycloSpec:
        if val not in s:
            consistent = False
            return consistent
        s.remove(val)
    return consistent

def LinearSpectrum(peptide):
    prefix_mass = [0]
    for i in range(1, len(peptide) + 1):
        temp = prefix_mass[i - 1] + integerMass[peptide[i - 1]]
        prefix_mass.append(temp)
    linear_spectrum = [0]
    for i in range(0, len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(linear_spectrum)

def CyclicSpectrum(peptide):
    prefix_mass = [0]
    for i in range(1, len(peptide) + 1):
        temp = prefix_mass[i - 1] + integerMass[peptide[i - 1]]
        prefix_mass.append(temp)
    peptide_mass = prefix_mass[len(peptide)]
    cyclo_spectrum = [0]
    for i in range(0, len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclo_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                cur = peptide_mass - (prefix_mass[j] - prefix_mass[i])
                cyclo_spectrum.append(cur)
    return sorted(cyclo_spectrum)

def getMassLst(am):
    massLst = []
    for c in am:
        mass = integerMass[c]
        massLst.append(mass)
    return massLst

def getUnique(lst):
    tempLst = []
    for val in lst:
        if val not in tempLst:
            tempLst.append(val)
    return tempLst

def cyclopeptideSequencing(spectrum):
    spectrum = spectrum.split(' ')
    spectrum = list(map(int, spectrum))
    spectrum.sort()
    spectrum = list(map(str, spectrum))
    candidatePeptides = [""]
    finalPeptides = []
    while len(candidatePeptides) > 0:
        candidatePeptides = expand(candidatePeptides)
        candidatePeptidesTemp = candidatePeptides.copy()
        for peptide in candidatePeptides:
            theoCycloSpec = cycloSpectrum(peptide)
            theoLinearSpec = linearSpectrum(peptide)
            if getWeight(peptide) == int(spectrum[-1]):
                if (theoCycloSpec == spectrum):
                    finalPeptides.append(getMassLst(peptide))
                candidatePeptidesTemp.remove(peptide)
            elif not isConsistent(theoLinearSpec, spectrum):
                candidatePeptidesTemp.remove(peptide)
        candidatePeptides = candidatePeptidesTemp.copy()
    finalPeptides = getUnique(finalPeptides)
    return finalPeptides

def formatPrint(lst):
    finalStr = ''
    for val in lst:
        valTemp = list(map(str, val))
        str1 = '-'.join(valTemp)
        finalStr += str1 + ' '
    return finalStr


#print(formatPrint(cyclopeptideSequencing("0 113 128 186 241 299 314 427")))