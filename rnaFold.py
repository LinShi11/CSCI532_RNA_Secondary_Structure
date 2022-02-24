import numpy as np
import pandas as pd


class rna:
    def __init__(self, rna):
        length = len(rna)
        self.table = pd.DataFrame(np.nan, index=range(length), columns=range(length))
        self.rna = rna
        for i in range(self.table.shape[0]):
            for j in range(5):
                if (i + j < self.table.shape[0]):
                    self.table.loc[i, i + j] = 0
                else:
                    break

    def fold(self):
        self.calculateFold(0, len(self.rna))
        print(self.table)
        print("The total score of fold:", str(self.table.loc[0, len(self.rna)-1]))


    def findMax(self, array):
        temp = 0
        for i in array:
            if i > temp:
                temp = i
        return temp

    def calculateFold(self, x, y):
        if (x >= y - 4):
            return 0
        elif (pd.notna(self.table.loc[x, y-1])):
            return self.table.loc[x, y-1]
        else:
            for i in range(y):
                for j in range(i-4):
                    tempMax = self.table.iloc[j, i - 1]
                    splitMax = 0
                    splitTempMax = [0]
                    if (self.rna[j] == "A" and self.rna[i] == "U") or (self.rna[j] == "U" and self.rna[i] == "A") or (self.rna[j] == "C" and self.rna[i] == "G") or (self.rna[j] == "G" and self.rna[i] == "C"):
                        for k in range(j, i+1):
                            one = self.calculateFold(j+1, k - 1)
                            two = self.calculateFold(k, i-1)
                            splitTempMax.append(1 + one + two)
                        splitMax = self.findMax(splitTempMax)
                    self.table.loc[j, i] = max(tempMax, splitMax)
        return splitMax