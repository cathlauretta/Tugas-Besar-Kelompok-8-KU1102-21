# Program Manajer Finansial Pribadi
# Suatu program untuk membantu pengguna dalam mengatur keuangan secara efektif dan otomatis

# KAMUS
# alokasi_wallet, alokasi_tabungan, alokasi_investasi   : float
# gaji, pilhan  	                                    : int
# bunga, pajak 		                                    : float
# saldo 			                                    : array [0..2] of float
# lanjut 			                                    : bool
# target, mode, lokasi, jenis setoran, t                : int
# nominal, tabungan, investasi                          : float
# penerima 			                                    : str
# konfirmasi			                                : int

# Definisi Prosedur alokasi
def alokasi(A,B,C):
    # menentukan alokasi dana berdasarkan parameter input

    # KAMUS LOKAL 
    # setuju : str
    # alokasi_wallet, alokasi_tabungan, alokasi_investasi : float

    # ALGORITMA
    global alokasi_wallet
    global alokasi_tabungan
    global alokasi_investasi
    print("Kami merekomendasikan alokasi keuangan sebagai berikut: \n1. Saldo sebesar {}% dari pendapatan. \n2. Tabungan sebesar {}% dari pendapatan. \n3. Investasi sebesar {}% dari pendapatan. \nApakah Anda setuju ?".format(A,B,C))
    setuju = str(input("Y/N : "))           # Pernyataan setuju atau tidak dengan program pengaturan keuangan yang ditawarkan
    if setuju == "Y" :
        alokasi_wallet = A/100
        alokasi_tabungan = B/100
        alokasi_investasi = C/100
    elif setuju =="N" :                     # Mengisi sendiri program pengaturan keuangan
        alokasi_wallet = float(input("Masukkan persentase saldo yang diinginkan: "))/100
        alokasi_tabungan = float(input("Masukkan persentase tabungan yang diinginkan: "))/100
        alokasi_investasi = float(input("Masukkan persentase investasi yang diinginkan: "))/100
    else :
        exit("Input invalid.")

    return
#=================================================================
# ALGORITMA PROGRAM UTAMA

# MULAI SET UP PERSONALISASI APLIKASI
#-----------------------------------------------------------------
# Menentukan proporsi alokasi dana berdasarkan pendapatan per bulan user
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
#-----------------------------------------------------------------
# Menentukan Bunga Investasi yang Diinginkan
print("\nBunga Investasi per tahun: \n1. Bunga deposito (pajak 20%): 3 % \n2. Bunga deposito valas (Dollar)(pajak 20%): 0.2 % \n3. Bunga tabungan emas (pajak 1%): 10 % ")
pilihan = int(input("Masukkan pilihan Anda: "))
if pilihan == 1 :
    bunga = 0.03
    pajak = 0.2
elif pilihan == 2 :
    bunga = 0.002
    pajak = 0.2
elif pilihan == 3 :
    bunga = 0.1
    pajak = 0.001
else :
    exit("Silakan pilih antara angka 1-3")

# SELESAI SET UP PERSONALISASI APLIKASI

#=================================================================
# MULAI PROGRAM UMUM

saldo = [0, 0, 0]   # Inisialisasi saldo awal user
# saldo[0] : saldo wallet
# saldo[1] : saldo tabungan
# saldo[2] : saldo investasi

# Looping Keberjalanan Program
lanjut = True
while lanjut == True:   
    # Looping Menu Utama selama Target (Tujuan Finansial) Belum Tercapai
    target = int(input("\nMasukkan target jumlah uang yang ingin dicapai: "))     # Target uang yang ingin dicapai dalam tabungan
    while saldo[1] + saldo[2] < target :
        print("==============================")
        print("Wallet : Rp{} | Tabungan : Rp{} | Investasi : Rp{}".format(saldo[0], saldo[1], saldo[2]))
        print("Mode :\n1. Setor\n2. Tarik\n3. Transfer/Bayar\n4. Tujuan Investasi")
        mode = int(input("Harap pilih angka:  "))
        #-----------------------------------------------------------------
        # Mode Setor
        if mode == 1 :
            lokasi = int(input("1. Wallet | 2. Tabungan | 3. Investasi | Pilih lokasi tujuan setoran: "))
            if lokasi == 1 :
                jenis_setoran = int(input("1. Income | 2. Lainnya | Pilih jenis setoran: "))
                nominal = float(input("Nominal setoran: "))
                if jenis_setoran == 1 : 
                    saldo[0] += nominal*alokasi_wallet
                    saldo[1] += nominal*alokasi_tabungan
                    saldo[2] += (1 - pajak) * saldo[2] * (bunga/12)
                    saldo[2] += nominal*alokasi_investasi
                elif jenis_setoran == 2 :  
                    saldo[0] += nominal
                else :
                    print("Input tidak valid.")
            elif lokasi == 2 :
                nominal = float(input("Nominal setoran: "))
                if nominal <= saldo[0] :
                    saldo[0] -= nominal
                    saldo[1] += nominal
                else :
                    print("Saldo tidak mencukupi.")
            elif lokasi == 3 :
                nominal = float(input("Nominal setoran: "))
                if nominal <= saldo[0] :
                    saldo[0] -= nominal
                    saldo[2] += nominal
                else :
                    print("Saldo tidak mencukupi.")
        #-----------------------------------------------------------------
        # Mode Tarik
        elif mode == 2 :
            lokasi = int(input("1. Saldo | 2. Tabungan | 3. Investasi | Pilih lokasi penarikan: "))
            nominal = float(input("Nominal tarikan: "))
            if lokasi == 1 and nominal <= saldo[0] :
                saldo[0] -= nominal
                print("Saldo berhasil ditarik dalam bentuk uang tunai.")
            elif lokasi == 2 and nominal <= saldo[1] : 
                saldo[1] -= nominal
                saldo[0] += nominal
                print("Tabungan berhasil dikonversikan ke saldo wallet.")
            elif lokasi == 3 and nominal <= saldo[2] :
                saldo[2] -= nominal 
                saldo[0] += nominal
                print("Investasi berhasil dikonversikan ke saldo wallet.")
            else :
                print("Input tidak valid.")
        #-----------------------------------------------------------------
        # Mode Transfer/Bayar
        elif mode == 3 :
            penerima = input("Masukkan nomor rekening penerima: ")
            nominal = float(input("Nominal transfer/pembayaran: "))
            if nominal <= saldo[0] :
                saldo[0] -= nominal
                print("Transfer Rp{} ke rekening {} berhasil dilakukan".format(nominal, penerima))
            else :
                print("Input tidak valid.")
        #-----------------------------------------------------------------
        # Mode Investasi 
        elif mode == 4:
            t = 0               # Waktu untuk mencapai tujuan finansial
            tabungan = saldo[1]
            investasi = saldo[2]

            while (tabungan + investasi) < target :
                t += 1
                tabungan += gaji * alokasi_tabungan
                investasi += (1 - pajak) * investasi * (bunga/12)
                investasi += gaji * alokasi_investasi

            print("Waktu yang dibutuhkan untuk mencapai tujuan finansial Anda adalah {} bulan.".format(t))
        
        #-----------------------------------------------------------------
        # Apabila input user tidak sesuai
        else :
            print("Input tidak valid.")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Target (Tujuan Finansial) Sudah Tercapai            
    print("==============================")
    print("Selamat! Tujuan finansial Anda telah tercapai.\nSilakan pilih opsi berikut:\n1. Buat tujuan finansial baru.\n2. Keluar.")
    konfirmasi = int(input("Masukkan pilihan Anda: "))
    if konfirmasi == 1 :
        print("Tabungan dan investasi Anda telah dikonversikan ke saldo wallet Anda.")
        saldo[0] += saldo[1]
        saldo[0] += saldo[2]
        saldo[1] = 0
        saldo[2] = 0
        lanjut = True
        
    elif konfirmasi == 2 :
        print("Terima kasih! Silakan tarik jumlah uang Anda sebesar Rp{}".format(saldo[0]+saldo[1]+saldo[2]))
        lanjut = False

# SELESAI PROGRAM UMUM