import numpy
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def figure5And6Data(path):
    path = path
    snps = []
    species = []
    maxSnps = 0

    with open(path) as inFile:
        line = inFile.readline()
        while line != "":
            if line[0] == '>':
                snpCount = 0
                snpLocation = []
                diffSpecies = 0
                reference = inFile.readline().strip().split()[1]
                for i in range(6):
                    line = inFile.readline().strip().split()[1]
                    if line != reference:
                        diffSpecies += 1
                    for j in range(len(reference)):
                        if reference[j] != line[j] and j not in snpLocation:
                            snpCount += 1
                            snpLocation.append(j)
                snps.append(snpCount)
                if snpCount > maxSnps:
                    maxSnps = snpCount
                species.append(diffSpecies)
            line = inFile.readline()

    sortedSnps = sorted(snps)
    sortedSpecies = sorted(species)

    print(str(numpy.mean(sortedSnps)))
    print(str(numpy.mean(sortedSpecies)))
    print(str(maxSnps))

    with open("snpsPerProbe.txt", 'w') as outFile:
        outFile.write("snps_per_probe\n")
        for snp in sortedSnps:
            outFile.write(str(snp) + '\n')

    with open("differentFromReference.txt", 'w') as outFile:
        outFile.write("different_from_reference\n")
        for species in sortedSpecies:
            outFile.write(str(species) + '\n')
    figure5Graph("snpsPerProbe.txt")
    figure6Graph("differentFromReference.txt")
    
def figure5Graph(figure5path):
    sns.set_theme(style="ticks", color_codes=True)
    df = pd.read_csv(figure5path, sep='\t')

    y = sns.histplot(data=df, x="snps_per_probe", binwidth=3)
    y.set(xlabel = "SNPs per probe", ylabel="Count")
    plt.show()
    plt.savefig("figure5")
    plt.clf()

def figure6Graph(figure6path):
    sns.set_theme(style="ticks", color_codes=True)
    df = pd.read_csv(figure6path, sep='\t')

    y = sns.histplot(data=df, x="different_from_reference", binwidth=1)
    y.set(xlabel = "Number of Different Species", ylabel="Probe Count")
    plt.show()
    plt.savefig("figure6")
    plt.clf()