import numpy
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def figure3Data(path):
    path = path
    with open(path) as inFile: 
        allLengths = []
        line = inFile.readline()
        count = 0
        while line != "":
            if line[0] == '>':
                line = line.strip().split(' ')
                allLengths.append(len(line[0]) + int(line[1]) + len(line[2]))
            line = inFile.readline()
    sortedLengths = sorted(allLengths)
    with open("probeInfo.txt", 'w') as outFile:
        outFile.write("Number of Probes: " + str(len(sortedLengths)) + '\n')
        outFile.write("Minimum Size of a Probe: " + str(min(sortedLengths)) + '\n')
        outFile.write("Maximum Size of a Probe: " + str(max(sortedLengths)) + '\n')
        outFile.write("Mean Size of a Probe: " + str(numpy.mean(sortedLengths)) + '\n')
    with open("probeLengths.txt", 'w') as outFile:
        outFile.write("probe_length\n")
        for length in sortedLengths:
            outFile.write(str(length) + '\n')
    figure3Graph("probeLengths.txt")

def figure3Graph(figure3path):
    sns.set_theme(style="ticks", color_codes=True)
    df = pd.read_csv(figure3path, sep='\t')

    y = sns.histplot(data=df, x="probe_length")
    y.set(xlabel = "Probe Lengths", ylabel="Count")
    y.set_xlim(0, 1500)
    plt.show()
    plt.savefig("figure3")
    plt.clf()