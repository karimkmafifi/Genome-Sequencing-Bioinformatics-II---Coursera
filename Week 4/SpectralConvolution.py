def spectralConvolution(sortedSpectrum):
    sortedSpectrum = sortedSpectrum.split(' ')
    diffLst = []
    for i in range(len(sortedSpectrum)):
        for j in range(i, len(sortedSpectrum)):
            diff = abs(int(sortedSpectrum[i])-int(sortedSpectrum[j]))
            if diff != 0:
                diffLst.append(diff)
    diffLst.sort()
    diffLst = map(str, diffLst)
    return ' '.join(diffLst)

#print(spectralConvolution('0 137 186 323'))
