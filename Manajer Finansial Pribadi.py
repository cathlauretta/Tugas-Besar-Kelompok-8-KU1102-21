# Program Financial Manager
# Suatu program untuk membantu pengguna dalam mengatur keuangan secara efektif

# KAMUS
# gaji : int (Input awal dari pendapatan tiap bulan)
# setuju : str
# alokasi_saldo, alokasi_tabungan, alokasi_investasi : float
# pilihan : int (Menentukan pilihan bunga investasi yang diinginkan)
# bunga, pajak : float
# saldo, tabungan, investasi : float
# lanjut : bool
# target : int
# mode, lokasi, jenis_setoran : int
# nominal : float
# penerima : str
# konfirmasi : str

def alokasi(A,B,C):
    global alokasi_saldo
    global alokasi_tabungan
    global alokasi_investasi
    print("Kami merekomendasikan alokasi keuangan sebagai berikut: \n1. Saldo sebesar {}% dari pendapatan. \n2. Tabungan sebesar {}% dari pendapatan. \n3. Investasi sebesar {}% dari pendapatan. \nApakah Anda setuju ?".format(A,B,C))
    setuju = str(input("Y/N : "))           # Pernyataan setuju atau tidak dengan program pengaturan keuangan yang ditawarkan
    if setuju == "Y" :
        alokasi_saldo = A/100
        alokasi_tabungan = B/100
        alokasi_investasi = C/100
    elif setuju =="N" :                     # Mengisi sendiri program pengaturan keuangan
        alokasi_saldo = float(input("Masukkan persentase saldo yang diinginkan: "))
        alokasi_tabungan = float(input("Masukkan persentase tabungan yang diinginkan: "))
        alokasi_investasi = float(input("Masukkan persentase investasi yang diinginkan: "))
    else :
        exit("Input invalid.")

# def setor(tempat) :
#     nominal = int(input("Nominal setoran: "))
#     tempat += nominal

#===============================================================
# Set up preferensi user
gaji = int(input("Masukkan pendapatan Anda tiap bulan: "))

if 0 < gaji <= 5000000 :
    alokasi(50, 30, 20)
elif 5000000 < gaji <= 20000000 :
    alokasi(40, 30, 30)
elif 20000000 < gaji <= 35000000 :
    alokasi(35, 30, 35)
elif 35000000 < gaji <= 50000000 :
    alokasi(30, 35, 35)
elif 50000000 < gaji <= 100000000 :
    alokasi(25, 35, 40)
elif gaji > 100000000:
    alokasi(20, 40, 40)
#===============================================================

# Menentukan Bunga Investasi yang Diinginkan
print("\nBunga Investasi per tahun: \n1. Bunga deposito (pajak 20%): 2.692 % \n2. Bunga deposito valas (Dollar)(pajak 20%): 0.204 % \n3. Bunga tabungan emas (pajak 0.9%): 10 % ")
pilihan = int(input("Masukkan pilihan Anda: "))
if pilihan == 1 :
    bunga = 0.02692
    pajak = 0.2
elif pilihan == 2 :
    bunga = 0.00204
    pajak = 0.2
elif pilihan == 3 :
    bunga = 0.1
    pajak = 0.009
else :
    print("Silakan pilih antara angka 1-3")
# ==============================================================

# Menu
saldo = 0                                       # Jumlah awal saldo
tabungan = 0                                    # Jumlah awal tabungan
investasi = 0                                   # Jumlah awal investasi
lanjut = True
while lanjut == True:
    target = int(input("\nMasukkan target jumlah uang yang ingin dicapai: "))     # Target uang yang ingin dicapai dalam tabungan
    while tabungan + investasi < target :
        print("==============================")
        print("Saldo : Rp{} | Tabungan : Rp{} | Investasi : Rp{}".format(saldo, tabungan, investasi))
        print("Mode :\n1. Setor\n2. Tarik\n3. Transfer/Bayar")
        mode = int(input("Harap pilih angka:  "))
        if mode == 1 :
            lokasi = int(input("1. Saldo | 2. Tabungan | 3. Investasi | Pilih lokasi setoran: "))
            if lokasi == 1 :
                jenis_setoran = int(input("1. Income | 2. Lainnya | Pilih jenis setoran: "))
                nominal = float(input("Nominal setoran: "))
                if jenis_setoran == 1 : 
                    saldo += nominal*alokasi_saldo
                    tabungan += nominal*alokasi_tabungan
                    investasi += (1 - pajak) * investasi * (bunga/12)
                    investasi += nominal*alokasi_investasi

                else :  
                    saldo += nominal
            elif lokasi == 2 :
                nominal = float(input("Nominal setoran: "))
                if nominal <= saldo :
                    saldo -= nominal
                    tabungan += nominal
                else :
                    print("Saldo tidak mencukupi.")
            elif lokasi == 3 :
                nominal = float(input("Nominal setoran: "))
                if nominal <= saldo :
                    saldo -= nominal
                    investasi += nominal
                else :
                    print("Saldo tidak mencukupi.")
        
        elif mode == 2 :
            lokasi = int(input("1. Saldo | 2. Tabungan | 3. Investasi | Pilih lokasi penarikan: "))
            nominal = float(input("Nominal tarikan: "))
            if lokasi == 1 and nominal <= saldo :
                saldo -= nominal
                print("Saldo berhasil ditarik dalam bentuk uang tunai.")
            elif lokasi == 2 and nominal <= tabungan : 
                tabungan -= nominal
                saldo += nominal
                print("Tabungan berhasil dikonversikan ke saldo.")
            elif lokasi == 3 and nominal <= investasi :
                investasi -= nominal 
                saldo += nominal
                print("Investasi berhasil dikonversikan ke saldo.")
            else :
                print("Input tidak valid.")

        elif mode == 3 :
            penerima = input("Masukkan nomor rekening penerima: ")
            nominal = float(input("Nominal transfer/pembayaran: "))
            if nominal <= saldo :
                saldo -= nominal
            else :
                print("Input tidak valid.")
                   
    print("==============================")
    print("Selamat! Tujuan finansial Anda telah tercapai.\nSilakan pilih opsi berikut:\n1. Buat tujuan finansial baru.\n2. Keluar.")
    konfirmasi = int(input("Masukkan pilihan Anda: "))
    if konfirmasi == 1 :
        saldo += tabungan
        saldo += investasi
        tabungan = 0
        investasi = 0
        print("Tabungan dan investasi Anda telah dikonversikan ke saldo Anda")
        lanjut = True
        
    elif konfirmasi == 2 :
        print("Terima kasih! Silakan tarik jumlah uang Anda sebesar Rp{}".format(saldo+tabungan+investasi))
        lanjut = False

# Selesai