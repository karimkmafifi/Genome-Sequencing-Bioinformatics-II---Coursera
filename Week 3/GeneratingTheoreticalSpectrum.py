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

def generateSubpeptides(aminoPep):
    subpeptides = []
    for i in range(1, len(aminoPep)):
        tempAminoPep = aminoPep+aminoPep[0:i]
        for j in range(0, len(tempAminoPep)-i):
            subpep = tempAminoPep[j:j+i]
            subpeptides.append(subpep)
    subpeptides.append(aminoPep)
    return subpeptides

def getWeight(aminoSubPep):
    weight = 0
    for am in aminoSubPep:
        weight += integerMass[am]
    return weight

def cyclospectrum(aminoPep):
    subpeptides = generateSubpeptides(aminoPep)
    spectrum = [0]
    for subpep in subpeptides:
        spectrum.append(getWeight(subpep))
    spectrum.sort()
    spectrum = map(str, spectrum)
    spectrum = ' '.join(spectrum)
    return spectrum
     
#print(cyclospectrum('TAIM'))