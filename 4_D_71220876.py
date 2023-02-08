print ('Nilai Ke 1')

harian = int(input('Masukkan nilai harian Anda : '))
Uts = int(input('Masukkan nilai Uts anda : '))
Uas = int(input('Masukkan nilai uas anda : '))

print ('Nilai Ke 2')
hariann = int(input('Masukkan nilai harian Anda : '))
Utss = int(input('Masukkan nilai Uts anda : '))
Uass = int(input('Masukkan nilai uas anda : '))

print ('Total Nilai')
nilai = (harian * 0.3 + Uts * 0.3 + Uas * 0.4) / 2
print ('Total Nilai yang didapat : ')
print ('Total Nilai dalam huruf : ')

if nilai >= 80 :
    print ('A')
elif nilai >= 60 :
    print ('B')
elif nilai >= 40 :
    print ('C')
elif nilai >= 20 :
    print ('D')
elif nilai >= 0 :
    print ('E')
