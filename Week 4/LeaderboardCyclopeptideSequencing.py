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
    
def leaderboardCyclopeptideSequencing(n, spectrum):
    spectrum = spectrum.split(' ')
    spectrum = list(map(int, spectrum))
    spectrum.sort()
    spectrum = list(map(str, spectrum))
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

#print(linearScoring('PEEP', '0 97 97 97 100 129 194 226 226 226 258 323 323 355 393 452'))
#print(leaderboardCyclopeptideSequencing(207, "0 71 87 87 87 87 97 101 101 103 113 114 115 128 128 129 131 131 131 137 147 156 158 163 174 188 188 199 210 217 218 226 230 243 243 243 244 245 245 248 252 256 262 266 284 286 289 294 317 327 327 330 330 332 335 339 341 348 371 373 374 375 380 380 385 397 399 401 414 414 417 418 425 435 436 440 442 461 470 472 472 488 488 500 501 508 511 511 515 527 527 528 529 529 538 548 565 571 573 575 579 587 591 598 601 616 616 619 628 628 635 641 642 642 655 657 658 662 662 666 678 688 702 702 715 726 729 733 738 744 747 753 754 755 756 759 764 765 772 773 775 789 799 813 816 817 827 836 841 843 852 859 860 861 865 875 885 886 890 900 906 909 912 914 914 914 928 944 945 952 964 968 972 973 981 983 989 990 996 999 1001 1001 1015 1016 1027 1037 1042 1043 1053 1055 1056 1059 1070 1073 1082 1088 1092 1102 1103 1104 1112 1127 1127 1129 1130 1143 1144 1155 1156 1157 1158 1169 1170 1174 1189 1190 1199 1200 1207 1213 1216 1226 1231 1241 1241 1244 1244 1255 1258 1261 1270 1274 1283 1286 1289 1300 1300 1303 1303 1313 1318 1328 1331 1337 1344 1345 1354 1355 1370 1374 1375 1386 1387 1388 1389 1400 1401 1414 1415 1417 1417 1432 1440 1441 1442 1452 1456 1462 1471 1474 1485 1488 1489 1491 1501 1502 1507 1517 1528 1529 1543 1543 1545 1548 1554 1555 1561 1563 1571 1572 1576 1580 1592 1599 1600 1616 1630 1630 1630 1632 1635 1638 1644 1654 1658 1659 1669 1677 1679 1683 1684 1685 1692 1701 1703 1708 1717 1727 1728 1731 1745 1755 1769 1771 1772 1779 1780 1785 1788 1789 1790 1791 1797 1800 1806 1811 1815 1818 1829 1842 1842 1856 1866 1878 1882 1882 1886 1887 1889 1902 1902 1903 1909 1916 1916 1925 1928 1928 1943 1946 1953 1957 1965 1969 1971 1973 1979 1996 2006 2015 2015 2016 2017 2017 2029 2033 2033 2036 2043 2044 2056 2056 2072 2072 2074 2083 2102 2104 2108 2109 2119 2126 2127 2130 2130 2143 2145 2147 2159 2164 2164 2169 2170 2171 2173 2196 2203 2205 2209 2212 2214 2214 2217 2217 2227 2250 2255 2258 2260 2278 2282 2288 2292 2296 2299 2299 2300 2301 2301 2301 2314 2318 2326 2327 2334 2345 2356 2356 2370 2381 2386 2388 2397 2407 2413 2413 2413 2415 2416 2416 2429 2430 2431 2441 2443 2443 2447 2457 2457 2457 2457 2473 2544"))