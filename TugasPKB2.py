import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel(
    'https://github.com/thoriqakhdn/FuzzyLogic/blob/main/bengkel.xlsx?raw=true')
data

# Membership Function Plot servis

# servis (Bagus)
servis_x_1 = [0, 60, 80, 100]
servis_y_1 = [0, 0, 1, 1]
plt.plot(servis_x_1, servis_y_1, label='Bagus', color='b')
plt.show()

# servis (Sedang)
servis_x_2 = [0, 20, 40, 60, 80, 100]
servis_y_2 = [0, 0, 1, 1, 0, 0]
plt.plot(servis_x_2, servis_y_2, label='Sedang', color='y')
plt.show()

# servis (Buruk)
servis_x_3 = [0, 20, 40, 100]
servis_y_3 = [1, 1, 0, 0]
plt.plot(servis_x_3, servis_y_3, label='Buruk', color='g')
plt.show()

# Combined Membership Function for servis
plt.plot(servis_x_1, servis_y_1, label='Bagus')
plt.plot(servis_x_2, servis_y_2, label='Sedang')
plt.plot(servis_x_3, servis_y_3, label='Buruk')
plt.show()


def score__high(n):
    if n > 80:
        return 1
    elif n <= 60:
        return 0
    else:
        return (n - 60) / (80-60)


def score__mid(n):
    if n > 80 or n <= 20:
        return 0
    elif n > 20 and n <= 40:
        return (n - 20) / (40 - 20)
    elif n > 40 and n <= 60:
        return 1
    elif n > 60 and n <= 80:
        return (80 - n) / (80 - 60)


def score__low(n):
    if n <= 20:
        return 1
    elif n > 40:
        return 0
    else:
        return (40 - n) / (40 - 20)


for i in range(len(data)):
    print(f"data ke {i} --> {data.iloc[i]['servis']}")
    print(f"high = {score__high(data.loc[i]['servis'])}")
    print(f"mid = {score__mid(data.loc[i]['servis'])}")
    print(f"low = {score__low(data.loc[i]['servis'])}")
    print('\n\n\n')

# Membership Function Plot harga

# harga (Murah)
harga_x_1 = [0, 6, 8.5, 10]
harga_y_1 = [0, 0, 1, 1]
plt.plot(harga_x_1, harga_y_1, label='Murah', color='b')
plt.show()

# harga (Sedang)
harga_x_2 = [0, 2, 4.5, 6.5, 8.5, 10]
harga_y_2 = [0, 0, 1, 1, 0, 0]
plt.plot(harga_x_2, harga_y_2, label='Sedang', color='y')
plt.show()

# harga (Buruk)
harga_x_3 = [0, 2, 4.5, 10]
harga_y_3 = [1, 1, 0, 0]
plt.plot(harga_x_3, harga_y_3, label='Mahal', color='g')
plt.show()

# Combined Membership Function for harga

plt.plot(harga_x_1, harga_y_1, label='Murah', color='b')
plt.plot(harga_x_2, harga_y_2, label='Sedang', color='y')
plt.plot(harga_x_3, harga_y_3, label='Mahal', color='g')


def score_harga_high(n):
    if n > 8.5:
        return 1
    if n <= 6:
        return 0
    return (n - 6) / (8.5 - 6)


def score_harga_mid(n):
    if n > 8 or n <= 2:
        return 0
    if n > 2 and n <= 4.5:
        return (n - 2) / (5 - 2)
    if n > 4.5 and n <= 6.5:
        return 1
    if n > 6.5 and n <= 8.5:
        return (8.5 - n) / (8.5 - 6.5)


def score_harga_low(n):
    if n <= 2:
        return 1
    if n > 4.5:
        return 0
    return (4.5 - n) / (4.5 - 2)


for i in range(len(data)):
    print(f"data ke {i} --> {data.iloc[i]['harga']}")
    print(f"high = {score_harga_high(data.iloc[i]['harga'])}")
    print(f"mid = {score_harga_mid(data.iloc[i]['harga'])}")
    print(f"low = {score_harga_low(data.iloc[i]['harga'])}")
    print('\n\n\n')

fuzzy = []

for i in range(len(data)):
    fuzzy.append([{'category': 'Sangat_bagus', 'score': min(score_harga_high(data.loc[i]['harga']), score__high(data.loc[i]['servis']))},
                  {'category': 'Sangat_bagus', 'score': min(score_harga_high(
                      data.loc[i]['harga']), score__mid(data.loc[i]['servis']))},
                  {'category': 'Sedang', 'score': min(score_harga_high(
                      data.loc[i]['harga']), score__low(data.loc[i]['servis']))},
                  {'category': 'Sangat_bagus', 'score': min(score_harga_mid(
                      data.loc[i]['harga']), score__high(data.loc[i]['servis']))},
                  {'category': 'Sedang', 'score': min(score_harga_mid(
                      data.loc[i]['harga']), score__mid(data.loc[i]['servis']))},
                  {'category': 'Sedang', 'score': min(score_harga_mid(
                      data.loc[i]['harga']), score__low(data.loc[i]['servis']))},
                  {'category': 'Sedang', 'score': min(score_harga_low(
                      data.loc[i]['harga']), score__high(data.loc[i]['servis']))},
                  {'category': 'Buruk', 'score': min(score_harga_low(
                      data.loc[i]['harga']), score__mid(data.loc[i]['servis']))},
                  {'category': 'Buruk', 'score': min(score_harga_low(data.loc[i]['harga']), score__low(data.loc[i]['servis']))}])
fuzzy

result = []
for i in range(len(fuzzy)):
    max_Sangat_bagus = 0
    max_Sedang = 0
    max_Buruk = 0
    for j in range(len(fuzzy[i])):
        if fuzzy[i][j]['category'] == 'Sangat_bagus':
            max_Sangat_bagus = max(max_Sangat_bagus, fuzzy[i][j]['score'])
            #print(fuzzy[i][j]['score'], max_Sangat_bagus)
        elif fuzzy[i][j]['category'] == 'Sedang':
            max_Sedang = max(max_Sedang, fuzzy[i][j]['score'])
            #print(fuzzy[i][j]['score'], max_Sedang)
        elif fuzzy[i][j]['category'] == 'Buruk':
            max_Buruk = max(max_Buruk, fuzzy[i][j]['score'])
            #print(fuzzy[i][j]['score'], max_Buruk)
    result.append([max_Sangat_bagus, max_Sedang, max_Buruk])

result


def sugeno(x, y, z):
    return ((x * 100) + (y * 70) + (z * 50)) / (x + y + z)


sugeno_result = []
for i in range(len(result)):
    #printf('Sangat_bagus = {result[i][0]}\nSedang = {result[i][1]}\nBuruk = {result[i][2]}')
    sugeno_result.append(sugeno(result[i][0], result[i][1], result[i][2]), )

sugeno_result

datanew = data
datanew['score'] = np.zeros(100)

for i in range(len(datanew)):
    datanew['score'][i] = sugeno_result[i]

datanew = datanew.sort_values(['score'], ascending=False)
datanew

datanew2 = datanew.drop(['id', 'servis', 'score'], axis=1)
datanew2[:10].to_excel('peringkat.xlsx', index=False, header=False)
datanew2[:10]
