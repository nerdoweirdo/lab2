import os.path
import re
import pandas as pd
import matplotlib.pyplot as plt

def genInfo(data):
    print(data.head(5))
    numColumns = data.shape[1]
    print("The number of columns: ", numColumns)
    nameColumn = data.columns.tolist()
    print("The headers of columns: ", nameColumn)
    for columns in data.columns:
        print('Type of data in ', columns, ' column: ', data[columns].dtype)
    numRows = data.shape[0]
    print('The number of rows: ', numRows)

def regionInfo(data):
    print(data.loc[data['ГОРОД/РЕГИОН'] == input('Input region to get info: ')])

def valuesBigger(data):
    print(data.loc[data['ЧИСЛО ЗАБОЛЕВШИХ'] > int(input("Input the number to get the info where the number of ill people is bigger: "))][['ГОРОД/РЕГИОН', 'ЧИСЛО ЗАБОЛЕВШИХ']])

def ranking(data):
    data.sort_values(by=['ЧИСЛО ЗАБОЛЕВШИХ'], ascending=[False], inplace=True)
    data_ill = data.copy()
    data.sort_values(by=['ЧИСЛО ВЫЗДОРОВЕВШИХ'], ascending=[False], inplace=True)
    data_recovered = data.copy()
    data.sort_values(by=['ЧИСЛО УМЕРШИХ'], ascending=[False], inplace=True)
    data_died = data.copy()
    maxIll = data_ill.nlargest(5, ['ЧИСЛО ЗАБОЛЕВШИХ'])[['ГОРОД/РЕГИОН', 'ЧИСЛО ЗАБОЛЕВШИХ']]
    maxRecovered = data_recovered.nlargest(5, ['ЧИСЛО ВЫЗДОРОВЕВШИХ'])[['ГОРОД/РЕГИОН', 'ЧИСЛО ВЫЗДОРОВЕВШИХ']]
    maxDied = data_died.nlargest(5, ['ЧИСЛО УМЕРШИХ'])[['ГОРОД/РЕГИОН', 'ЧИСЛО УМЕРШИХ']]
    minIll = data_ill.nsmallest(5, ['ЧИСЛО ЗАБОЛЕВШИХ'])[['ГОРОД/РЕГИОН', 'ЧИСЛО ЗАБОЛЕВШИХ']]
    minRecovered = data_recovered.nsmallest(5, ['ЧИСЛО ВЫЗДОРОВЕВШИХ'])[['ГОРОД/РЕГИОН', 'ЧИСЛО ВЫЗДОРОВЕВШИХ']]
    minDied = data_died.nsmallest(5, ['ЧИСЛО УМЕРШИХ'])[['ГОРОД/РЕГИОН', 'ЧИСЛО УМЕРШИХ']]
    plt.figure(figsize=(15, 4))
    plt.subplot(2, 3, 1)
    plt.tight_layout()
    plt.title("Наибольшие по заболеваниям")
    plt.barh(maxIll['ГОРОД/РЕГИОН'], maxIll['ЧИСЛО ЗАБОЛЕВШИХ'])
    plt.subplot(2, 3, 2)
    plt.tight_layout()
    plt.title("Наибольшие по выздоровлениям")
    plt.barh(maxRecovered['ГОРОД/РЕГИОН'], maxRecovered['ЧИСЛО ВЫЗДОРОВЕВШИХ'])
    plt.subplot(2, 3, 3)
    plt.tight_layout()
    plt.title("Наибольшие по числу умерших")
    plt.barh(maxDied['ГОРОД/РЕГИОН'], maxDied['ЧИСЛО УМЕРШИХ'])
    plt.subplot(2, 3, 4)
    plt.tight_layout()
    plt.title("Наименьшие по заболеваниям")
    plt.barh(minIll['ГОРОД/РЕГИОН'], minIll['ЧИСЛО ЗАБОЛЕВШИХ'])
    plt.subplot(2, 3, 5)
    plt.tight_layout()
    plt.title("Наименьшие по выздоровлениям")
    plt.barh(minRecovered['ГОРОД/РЕГИОН'], minRecovered['ЧИСЛО ВЫЗДОРОВЕВШИХ'])
    plt.subplot(2, 3, 6)
    plt.tight_layout()
    plt.title("Наименьшие по числу умерших")
    plt.barh(minDied['ГОРОД/РЕГИОН'], minDied['ЧИСЛО УМЕРШИХ'])
    plt.show()

if __name__ == '__main__':
    Path = input("Input path to the file: ")
    flag = True
    if (os.path.exists(Path) == False or re.search(r'\.csv$', Path) == False):
        print("File does not exist or wrong extension.\n")
    else:
        global data
        data = pd.read_csv(Path, sep=',')
        genInfo(data)
        regionInfo(data)
        valuesBigger(data)
        ranking(data)