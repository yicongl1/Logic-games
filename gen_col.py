def DimacImage(graphMatrix): 
    numColor = 3
    numRows = len(graphMatrix)
    for i in range(numRows):
        numCols = len(graphMatrix[i])
        for j in range(numCols):
            for k in range(numColor):
                s = f'{-i*numColor+k} {-graphMatrix[i][j]*numColor+k} 0'
