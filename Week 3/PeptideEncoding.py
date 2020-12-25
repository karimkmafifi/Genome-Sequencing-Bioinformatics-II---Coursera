geneticCode = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",\
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",\
    "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",\
    "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",\
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",\
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",\
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",\
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",\
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",\
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",\
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",\
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",\
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",\
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",\
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",\
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def reverseComplement(dnaSeq):
    eq_nuc = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    dnaSeqRev = ''
    for i in range(len(dnaSeq)-1, -1, -1):
        dnaSeqRev += eq_nuc[dnaSeq[i]]
    return dnaSeqRev

def proteinTranslation(rnaPattern):
    aminoSeq = ''
    for i in range(0, len(rnaPattern), 3):
        amino = geneticCode[rnaPattern[i:i+3]]
        if amino != "*":
            aminoSeq += amino
    return aminoSeq

def proteinEncoding(dnaSeq, aminoPep):
    encodingDNAPep = []
    jump = len(aminoPep)*3
    
    for i in range(0, len(dnaSeq), 1):
        if i < len(dnaSeq)-jump+1:
            codonsSeq = dnaSeq[i:i+jump]
            revCodonsSeq = reverseComplement(codonsSeq)
            
            rnaCodonsSeq = codonsSeq.replace("T", "U")
            rnaRevCodonsSeq = revCodonsSeq.replace("T", "U")
            
            aminoSeq = proteinTranslation(rnaCodonsSeq)
            if aminoSeq == aminoPep:
                encodingDNAPep.append(codonsSeq)
                
            aminoSeq = proteinTranslation(rnaRevCodonsSeq)
            if aminoSeq == aminoPep:
                encodingDNAPep.append(codonsSeq)
                
    return '\n'.join(encodingDNAPep)
    
#print(proteinEncoding('ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA', 'MA'))