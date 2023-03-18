nilai_IPA = { 'Joni' : 9,
              'Kevin' : 8,
              'Dimas' : 7,
              'Dwi'   : 9,
              'Siska' : 7,
              'Dion'  : 8
}
nama = input ("Masukkan Nama Anda : ")
if nama in nilai_IPA :
    print ("Nilai IPA", nama, "adalah", nilai_IPA[nama])
else:
    print("Data anda tidak ditemukan.")
    print("Berikut data siswa :")
    for i in nilai_IPA.keys():
        print(i)