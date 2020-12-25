integerMass = {}

def topSpectralConvolution(m, sortedSpectrum):
    diffLst = []
    for i in range(len(sortedSpectrum)):
        for j in range(i, len(sortedSpectrum)):
            diff = abs(int(sortedSpectrum[i])-int(sortedSpectrum[j]))
            if diff != 0:
                diffLst.append(diff)

    diffLstTemp = []
    for val in diffLst:
        if val >= 57 and val <= 200:
            diffLstTemp.append(val)
    diffLst = diffLstTemp    
    diffLst = list(map(str, diffLst))
    
    diffLst2 = list(set(diffLst))
    diffLstCount = []
    for val in diffLst2:
        diffLstCount.append(diffLst.count(val))
    
    diffLst2 = [x for _,x in sorted(zip(diffLstCount, diffLst2), reverse=True)]
    diffLstCount.sort(reverse=True)
    print(diffLst2)
    for j in range(m, len(diffLst2)):
        if diffLstCount[j] < diffLstCount[m-1]:
            diffLst2 = diffLst2[:j]
            break
        
    chars = []
    for code in range(ord('A'), ord('Z') + 1):
        chars.append(chr(code))
    
    for code in range(ord('a'), ord('z') + 1):
        chars.append(chr(code))
    
    for val in diffLst2:
        amVal = chars.pop()
        integerMass[amVal] = int(val)

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

def generateSubpeptides(aminoPep):
    subpeptides = []
    for i in range(1, len(aminoPep)):
        tempAminoPep = aminoPep+aminoPep[0:i]
        for j in range(0, len(tempAminoPep)-i):
            subpep = tempAminoPep[j:j+i]
            subpeptides.append(subpep)
    subpeptides.append(aminoPep)
    return subpeptides

def cycloSpectrum(aminoPep):
    subpeptides = generateSubpeptides(aminoPep)
    spectrum = [0]
    for subpep in subpeptides:
        spectrum.append(getWeight(subpep))
    spectrum.sort()
    spectrum = map(str, spectrum)
    spectrum = ' '.join(spectrum)
    return spectrum

def cyclopeptideScoring(peptide, spectrum):
    peptideSpectrum = cycloSpectrum(peptide)
    peptideSpectrum = peptideSpectrum.split(' ')
    tempSpectrum = spectrum.split(' ')
    
    score = 0
    for i in range(len(peptideSpectrum)):
        if peptideSpectrum[i] in tempSpectrum:
            score += 1
            tempSpectrum.remove(peptideSpectrum[i])      
    return score

def generateSubpeptidesLinear(aminoPep):
    subpeptides = []
    for i in range(1, len(aminoPep)):
        tempAminoPep = aminoPep
        for j in range(0, len(tempAminoPep)-i):
            subpep = tempAminoPep[j:j+i]
            subpeptides.append(subpep)
    subpeptides.append(aminoPep)
    return subpeptides

def linearSpectrum(aminoPep):
    subpeptides = generateSubpeptidesLinear(aminoPep)
    spectrum = [0]
    for subpep in subpeptides:
        spectrum.append(getWeight(subpep))
    spectrum.sort()
    spectrum = map(str, spectrum)
    spectrum = ' '.join(spectrum)
    return spectrum

def linearScoring(peptide, spectrum):
    peptideSpectrum = linearSpectrum(peptide)
    peptideSpectrum = peptideSpectrum.split(' ')
    tempSpectrum = spectrum.split(' ')    
    score = 0
    for i in range(len(peptideSpectrum)):
        if peptideSpectrum[i] in tempSpectrum:
            score += 1
            tempSpectrum.remove(peptideSpectrum[i])      
    return score

def trim(leaderboard, spectrum, n):
    scores = []
    for pep in leaderboard:
        scr = linearScoring(pep, spectrum)
        scores.append(scr)
    
    leaderboard = [x for _,x in sorted(zip(scores, leaderboard), reverse=True)]
    scores.sort(reverse=True)
    
    for j in range(n, len(leaderboard)):
        if scores[j] < scores[n-1]:
            leaderboard = leaderboard[:j]
            return leaderboard
    return leaderboard

def getMass(am):
    massPep = []
    for c in am:
        mass = str(integerMass[c])
        massPep.append(mass)
    massPep = '-'.join(massPep)
    return massPep
    
def convolutionCyclopeptideSequencing(m, n, spectrum):
    spectrum = spectrum.split(' ')
    spectrum = list(map(int, spectrum))
    spectrum.sort()
    spectrum = list(map(str, spectrum))
    topSpectralConvolution(m, spectrum)
    leaderboard = ['']
    LeaderPeptide = ''
    while len(leaderboard) > 0:
        leaderboard = expand(leaderboard)
        leaderboardTemp = leaderboard.copy()
        for peptide in leaderboard:
            if getWeight(peptide) == int(spectrum[-1]):
                if cyclopeptideScoring(peptide, ' '.join(spectrum)) > cyclopeptideScoring(LeaderPeptide, ' '.join(spectrum)):
                    LeaderPeptide = peptide
            elif getWeight(peptide) > int(spectrum[-1]):
                leaderboardTemp.remove(peptide)
        leaderboard = leaderboardTemp.copy()
        leaderboard = trim(leaderboard, ' '.join(spectrum), n)
    return getMass(LeaderPeptide)

#print(topSpectralConvolution(20, list('0 57 118 179 236 240 301'.split(' '))))
#print(convolutionCyclopeptideSequencing(17, 322, '0 57 71 87 87 87 113 113 115 128 129 137 158 158 163 170 186 202 215 216 242 243 245 250 250 252 276 287 314 321 329 330 333 339 356 363 365 371 374 379 400 401 408 420 434 452 458 466 467 484 487 491 494 516 519 521 537 537 571 573 578 580 581 581 606 624 647 650 650 652 653 668 677 686 707 709 710 734 734 739 739 763 764 766 787 796 805 820 821 823 823 826 849 867 892 892 893 895 900 902 936 936 952 954 957 979 982 986 989 1006 1007 1015 1021 1039 1053 1065 1072 1073 1094 1099 1102 1108 1110 1117 1134 1140 1143 1144 1152 1159 1186 1197 1221 1223 1223 1228 1230 1231 1257 1258 1271 1287 1303 1310 1315 1315 1336 1344 1345 1358 1360 1360 1386 1386 1386 1402 1416 1473'))
    