import pandas as pd
import random

import xlwt
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel(
    'https://github.com/thoriqakhdn/FuzzyLogic/blob/main/bengkel.xlsx?raw=true')
data


def fuzifikasiservis(servis):
    if servis <= 35:
        hasil = [['kurang baik', 1]]
    elif servis > 35 and servis < 55:
        x = -(servis-55)/(55-35)
        y = (servis-35)/(55-35)
        hasil = [['kurang baik', x], ['cukup baik', y]]
    elif servis == 55:
        hasil = [['cukup baik', 1]]
    elif servis > 55 and servis < 75:
        x = -(servis-75)/(75-55)
        y = (servis-55)/(75-55)
        hasil = [['cukup baik', x], ['baik', y]]
    elif servis == 75:
        hasil = [['baik', 1]]
    elif servis > 75 and servis < 90:
        x = -(servis-90)/(90-75)
        y = (servis-75)/(90-75)
        hasil = [['baik', x], ['sangat baik', y]]
    elif servis >= 90:
        hasil = [['sangat baik', 1]]
    return hasil


def fuzifikasiharga(harga):
    if harga <= 3:
        hasil = [['murah', 1]]
    elif harga > 3 and harga < 6:
        x = -(harga-6)/(6-3)
        y = (harga-3)/(6-3)
        hasil = [['murah', x], ['sedang', y]]
    elif harga == 6:
        hasil = [['sedang', 1]]
    elif harga > 6 and harga < 9:
        x = -(harga-9)/(9-6)
        y = (harga-6)/(9-6)
        hasil = [['sedang', x], ['mahal', y]]
    elif harga >= 9:
        hasil = [['mahal', 1]]
    return hasil


def fuzifikasi(servis, harga):
    hasilservis = fuzifikasiservis(servis)
    hasilharga = fuzifikasiharga(harga)
    hasil = hasilservis + hasilharga
    return hasil


def fuzifikasicon(nilai1, nilai2):
    if nilai1[0] == 'kurang baik' and nilai2[0] == 'murah':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'kurang baik' and nilai2[0] == 'sedang':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'kurang baik' and nilai2[0] == 'mahal':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'cukup baik' and nilai2[0] == 'murah':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'cukup baik' and nilai2[0] == 'sedang':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'cukup baik' and nilai2[0] == 'mahal':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'baik' and nilai2[0] == 'murah':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'baik' and nilai2[0] == 'sedang':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'baik' and nilai2[0] == 'mahal':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['tinggi', nilai]
    if nilai1[0] == 'sangat baik' and nilai2[0] == 'murah':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'sangat baik' and nilai2[0] == 'sedang':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['rendah', nilai]
    if nilai1[0] == 'sangat baik' and nilai2[0] == 'mahal':
        if nilai1[1] < nilai2[1]:
            nilai = nilai1[1]
        else:
            nilai = nilai2[1]
        nk = ['tinggi', nilai]
    return nk


def fuzifikasidis(hasilcon):
    rendah = []
    tinggi = []
    hasil = []
    maxrendah = 0
    maxtinggi = 0
    for nilai in hasilcon:
        if nilai[0] == 'rendah':
            rendah.append(nilai)
        else:
            tinggi.append(nilai)
    if len(rendah) != 0:
        for nilai in rendah:
            if nilai[1] > maxrendah:
                maxrendah = nilai[1]
    hasil.append(['rendah', maxrendah])
    if len(tinggi) != 0:
        for nilai in tinggi:
            if nilai[1] > maxtinggi:
                maxtinggi = nilai[1]
    hasil.append(['tinggi', maxtinggi])
    return hasil


def inferensi(nilaifuzzy):
    con = []
    i = 0
    while i < 2:
        if nilaifuzzy[i][0] == 'murah' or nilaifuzzy[i][0] == 'sedang' or nilaifuzzy[i][0] == 'mahal':
            break
        j = 1
        while j < (len(nilaifuzzy)):
            if nilaifuzzy[j][0] == 'kurang baik' or nilaifuzzy[j][0] == 'cukup baik' or nilaifuzzy[j][0] == 'baik' or nilaifuzzy[j][0] == 'sangat baik':
                j += 1
            con.append(fuzifikasicon(nilaifuzzy[i], nilaifuzzy[j]))
            j += 1
        i += 1
    return fuzifikasidis(con)


def defuzifikasi(hasilinferensi):
    rendah = [10, 20, 30, 40, 50]
    antara = [60, 70]
    tinggi = [80, 90, 100]
    totalren, totalteng, totalteng1, totalteng2, totalting, penyebutteng = 0, 0, 0, 0, 0, 0
    if len(hasilinferensi) == 1:
        if hasilinferensi[0][0] == 'rendah':
            nkrendah = hasilinferensi[0][1]
        elif hasilinferensi[0][0] == 'tinggi':
            nktinggi = hasilinferensi[0][1]
    else:
        nkrendah = hasilinferensi[0][1]
        nktinggi = hasilinferensi[1][1]

    for nilai in rendah:
        totalren += nilai
    totalren = totalren * nkrendah

    for nilai in antara:
        x = -(nilai-80)/(80-50)
        y = (nilai-50)/(80-50)
        if nkrendah > x or nktinggi > y:
            totalteng1 = nilai*x
            totalteng2 = nilai*y
            if totalteng1 > totalteng2:
                totalteng += totalteng1
                penyebutteng += x
            else:
                totalteng += totalteng2
                penyebutteng += y
        else:
            totalteng1 = nilai*nkrendah
            totalteng2 = nilai*nktinggi
            if totalteng1 > totalteng2:
                totalteng += totalteng1
                penyebutteng += nkrendah
            else:
                totalteng += totalteng2
                penyebutteng += nktinggi
    for nilai in tinggi:
        totalting += nilai
    totalting = totalting * nktinggi
    pembilang = totalren+totalteng+totalting
    penyebut = (nkrendah*len(rendah))+penyebutteng+(nktinggi*len(tinggi))
    hasil = pembilang/penyebut
    return hasil


calon = []
for i in range(100):
    nilai = fuzifikasi(data['servis'][i], data['harga'][i])
    nk = inferensi(nilai)
    calon.append([i+1, defuzifikasi(nk)])
hasil = sorted(calon, key=lambda x: x[1], reverse=True)
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('bengkel')

row = 1

worksheet.write(0, 0, 'id')
worksheet.write(0, 1, 'Score')

for i in range(10):
    worksheet.write(row, 0, hasil[i][0])
    worksheet.write(row, 1, hasil[i][1])
    row += 1

workbook.save('peringkat.xls')
