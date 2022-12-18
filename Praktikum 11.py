# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:57:33 2022

@author: acer
"""

class Prak11:
    
    def __init__(self, nama, nilai):
        self.nama = nama
        self._nilai = nilai
        
    @property
    def detail(self):
        return "Nama: {} \nNilai: {}".format(self.nama, self._nilai)
    
    @property
    def nilai(self):
        pass
    
    @nilai.getter
    def nilai(self):
        return self._nilai
    
    @nilai.setter
    def nilai(self, input):
        self._nilai = input
        
    @nilai.deleter
    def nilai(self):
        self._nilai = None
        
        
def banner():
    print("----- Program Prak11 -----")
    print("1. Mendeklarasikan objek")
    print("2. Menampilkan objek")
    print("3. Merubah nilai objek")
    print("4. Menghapus objek")
    print("5. Keluar dari program\n")
    
def main():
    mahasiswa = Prak11(None, None)
    F = False
    while(not F):
        banner()
        pilihan = int(input("Masukkan pilihan berupa angka (1/2/3/4/5): "))
        if(pilihan == 1):
            nama = input("Masukkan namamu: ")
            nilai = int(input("Masukkan nilaimu: "))
            mahasiswa = Prak11(nama, nilai)
            print("Data berhasil ditambahkan")
            print("\n")
        elif(pilihan == 2):
            print("\n")
            print(mahasiswa.detail)
            print("\n")
        elif(pilihan == 3):
            opsi = input("Apa yang ingin anda diubah (Nama/Nilai): ")
            if(opsi == "Nama" or opsi == "nama"):
                nama = input("masukkan nama: ")
                mahasiswa.nama = nama
                print("Data nama berhasil diubah")
                print("\n")
            elif(opsi == "Nilai" or opsi == "nilai"):
                nilai = int(input("masukkan nilai: "))
                mahasiswa.nilai = nilai
                print("Data nilai berhasil diubah")
                print("\n")
            else:
                print("Masukkan opsi yang sesuai antara Nama/Nilai")
                print("\n")
        elif(pilihan == 4):
            mahasiswa.nama = None
            del mahasiswa.nilai
            print("Data berhasil dihapus")
            print("\n")
        elif(pilihan == 5):
            print("Terima kasih sudah menggunakan program saya!")
            F = True
        else:
            print("Masukkan angka yang sesuai dengan yang ada di menu")
            print("\n")
            
            
main()