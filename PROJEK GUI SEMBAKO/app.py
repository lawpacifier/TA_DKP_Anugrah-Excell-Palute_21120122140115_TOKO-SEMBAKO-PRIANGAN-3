from tkinter import *
from tkinter import ttk
import time
import os

root = Tk()
root.minsize(height=500, width=800)
root.maxsize(height=500, width=800)
root.title('TOKO SEMBAKO PRIANGAN 3')

running = False
total_ = []
hstr = []
#MEMBUAT WAKTU YANG TERJADI DI SEKARANG
def waktu(i):
    a = time.localtime()
    taggal = a.tm_mday
    bulan = a.tm_mon
    tahun = a.tm_year
    menit = a.tm_min
    jam = a.tm_hour
    waktu_terkini = str(taggal)+'/'+str(bulan)+'/' + \
        str(tahun)+' '+str(jam)+':'+str(menit)
    return waktu_terkini

def menuUtama():
    for widget in root.winfo_children():
        widget.destroy()

    def show_db():
            for widget in root.winfo_children():
                widget.destroy()
                
                #MENAMPILKAN ISI YANG ADA DIDALAM TAMPILAN DATA BARANG 
            labelframeHstr = LabelFrame(root, text='Tampilan Data Barang', font=(
                'Supermercado One', 15, 'bold'), bg='#4CAF50')
            labelframeHstr.grid(column=0, row=0, pady=20,
                                padx=42, sticky="wens")

            treeHstr1 = ttk.Treeview(labelframeHstr, height=10)
            treeHstr1['show'] = 'headings'

            s = ttk.Style(root)
            s.theme_use('clam')
            s.configure("Treeview.Heading", font=(
                'Supermercado One', 13, 'bold'))
            s.configure("Treeview", font=(
                'Supermercado One', 12, 'bold'), rowheight=25)

            treeHstr1['show'] = 'headings'
            treeHstr1['columns'] = (
                'No.', 'Kode Barang', 'Nama Barang', 'Harga Barang', 'Stok Barang')
            treeHstr1.column('No.', width=50, minwidth=50, anchor=CENTER)
            treeHstr1.column('Kode Barang', width=130,
                             minwidth=130, anchor=CENTER)
            treeHstr1.column('Nama Barang', width=300,
                             minwidth=300, anchor=CENTER)
            treeHstr1.column('Harga Barang', width=120,
                             minwidth=120, anchor=CENTER)
            treeHstr1.column('Stok Barang', width=80,
                             minwidth=80, anchor=CENTER)

            treeHstr1.heading('No.', text='No.', anchor=CENTER)
            treeHstr1.heading('Kode Barang', text='Kode', anchor=CENTER)
            treeHstr1.heading('Nama Barang', text='Nama Barang', anchor=CENTER)
            treeHstr1.heading(
                'Harga Barang', text='Harga (Rp.)', anchor=CENTER)
            treeHstr1.heading('Stok Barang', text='Stok', anchor=CENTER)

            file = open('data/dataBarang', 'r').readlines()
            file_r = open('data/dataBarang', 'r').readlines()
            data_listHstr = []
            for i in file:
                list = []
                a = i.replace('\n', '')
                a = a.split('|')
                list.extend(a)
                data_listHstr.append(list)
            indek = 0
            nomor = 1
            line = 0
            for a in file_r:
                i = data_listHstr[line]
                treeHstr1.insert('', indek, text='', values=(
                    nomor, i[0], i[1], i[2], i[3]))
                indek += 1
                line += 1
                nomor += 1
            hsbAdmin1 = ttk.Scrollbar(labelframeHstr)
            hsbAdmin1.configure(command=treeHstr1.yview)
            treeHstr1.configure(yscrollcommand=hsbAdmin1.set)
            hsbAdmin1.pack(side=RIGHT, fill=Y)
            treeHstr1.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

            buttonkembali = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                                   activebackground='#CCCCCC', activeforeground='black', width=15, command=menuUtama, bg='#e9f542')
            buttonkembali.place(relx=0.5, rely=0.8, anchor=CENTER)
    
    def exit_app():
        root.destroy()
        #MENAMPILKAN MENU TRANSASKI "PESANAN ANDA"
        
    def menuTransaksi():
        for widget in root.winfo_children():
            widget.destroy()
        header2 = Label(root, text='PESANAN ANDA', font=(
            'Supermercado One', 15, 'bold'), bg='#CCCCCC')
        label_kodebarang = Label(root, text='Kode Barang', font=(
            'Supermercado One', 13, 'bold'))
        label_jmlbarang = Label(root, text='Jumlah Barang', font=(
            'Supermercado One', 13, 'bold'))
        titik_kodebarang = Label(root, text=':', font=(
            'Supermercado One', 13, 'bold'))
        titik_jmlbarang = Label(root, text=':', font=(
            'Supermercado One', 13, 'bold'))
        ktk_namabarang = Entry(root, textvariable=data1, font=(
            'Supermercado One', 13, 'bold'), width=13, bg='#CCCCCC')
        ktk_jmlbarang = Entry(root, textvariable=data2, font=(
            'Supermercado One', 13, 'bold'), width=13, bg='#CCCCCC')

        #FUNGSI UNTUK MEMBUAT KERANJANG
        def Keranjang():
            kodebarang = data1.get()
            jmlbarang = data2.get()
            fileBarang = open('data/dataBarang', 'r')

            for i in fileBarang:
                list = []
                a = i.replace('\n', '')
                a = a.split('|')
                list.extend(a)
                kodebarang_ = list[0]
                stokbarang_ = list[3]
                if kodebarang == kodebarang_:
                    if jmlbarang == '':
                        menuTransaksi()
                        label_err1 = Label(root, text='(GAGAL) Jumlah Barang Tidak Boleh Kosong!!', font=(
                            'Supermercado One', 8, 'bold'), fg='#d10f0f', bg='#F0F0F0')
                        label_err1.place(relx=0.5, rely=0.4, anchor=CENTER)
                        break
                    else:
                        if int(stokbarang_) == 0:
                            label_err3 = Label(root, text='(GAGAL) Stok Barang HABIS !!', font=(
                                'Supermercado One', 8, 'bold'), fg='#d10f0f', bg='#F0F0F0')
                            label_err3.place(relx=0.5, rely=0.4, anchor=CENTER)
                            break
                        elif int(jmlbarang) > int(stokbarang_):
                            label_err2 = Label(root, text='(GAGAL) Jumlah Barang Melebihi Stok Yang tersedia...Sisa Stok (' +
                                               stokbarang_+')!!', font=('Supermercado One', 8, 'bold'), fg='#d10f0f', bg='#F0F0F0')
                            label_err2.place(relx=0.5, rely=0.4, anchor=CENTER)
                            break
                        else:
                            file = open('data/dataKeranjang', 'r')
                            y = len(file.readlines())
                            file_ = open('data/dataKeranjang', 'a')
                            write = list[0]+'|'+list[1]+'|' + \
                                list[2]+'|'+list[3]+'|'+jmlbarang

                            hrga_total = int(jmlbarang)*int(list[2])
                            write_history = list[0]+'|'+list[1]+'|' + \
                                jmlbarang+'|'+str(hrga_total)+'|'+waktu(0)
                            hstr.append(write_history)

                            if y < 1:
                                file_.write('')
                                file_.write(write)
                                file_.close()
                                file.close()
                                menuTransaksi()
                                label_suc = Label(root, text='(BERHASIL) Barang Berhasil Dimasukan dalam Keranjang !!', font=(
                                    'Supermercado One', 8, 'bold'), fg='#1fab34')
                                label_suc.place(
                                    relx=0.5, rely=0.4, anchor=CENTER)
                                break
                            elif y > 0:
                                file_.write('\n')
                                file_.write(write)
                                file_.close()
                                file.close()
                                menuTransaksi()
                                label_suc = Label(root, text='(BERHASIL) Barang Berhasil Dimasukan dalam Keranjang !!', font=(
                                    'Supermercado One', 8, 'bold'), fg='#1fab34')
                                label_suc.place(
                                    relx=0.5, rely=0.4, anchor=CENTER)
                                break
            else:
                menuTransaksi()
                label_err = Label(root, text='(GAGAL) Kode Barang Tidak Terdaftar !!', font=(
                    'Supermercado One', 8, 'bold'), fg='#d10f0f', bg='#F0F0F0')
                label_err.place(relx=0.5, rely=0.4, anchor=CENTER)

        #MEMBUAT TOTAL BELANJA
        def Total():
            for widget in root.winfo_children():
                widget.destroy()
            labelframe = LabelFrame(root, text='Total Belanja', font=(
                'Supermercado One', 15, 'bold'), bg='#CCCCCC')
            labelframe.grid(column=0, row=0, pady=20, padx=42, sticky="wens")

            tree = ttk.Treeview(labelframe, height=6)
            tree['show'] = 'headings'

            s = ttk.Style(root)
            s.theme_use('clam')
            s.configure("Treeview.Heading", font=(
                'Supermercado One', 13, 'bold'))
            s.configure("Treeview", font=(
                'Supermercado One', 12, 'bold'), rowheight=25)

            tree['show'] = 'headings'
            tree['columns'] = ('No.', 'Kode Barang',
                               'Nama Barang', 'Harga Barang', 'Jumlah Barang')
            tree.column('No.', width=50, minwidth=50, anchor=CENTER)
            tree.column('Kode Barang', width=130, minwidth=130, anchor=CENTER)
            tree.column('Nama Barang', width=300, minwidth=300, anchor=CENTER)
            tree.column('Harga Barang', width=120, minwidth=120, anchor=CENTER)
            tree.column('Jumlah Barang', width=80, minwidth=80, anchor=CENTER)

            tree.heading('No.', text='No.', anchor=CENTER)
            tree.heading('Kode Barang', text='Kode', anchor=CENTER)
            tree.heading('Nama Barang', text='Nama Barang', anchor=CENTER)
            tree.heading('Harga Barang', text='Harga (Rp.)', anchor=CENTER)
            tree.heading('Jumlah Barang', text='Jumlah', anchor=CENTER)

            file = open('data/dataKeranjang', 'r').readlines()
            file_r = open('data/dataKeranjang', 'r').readlines()
            data_listHstr = []
            for i in file:
                list = []
                a = i.replace('\n', '')
                a = a.split('|')
                list.extend(a)
                data_listHstr.append(list)
            indek = 0
            nomor = 1
            line = 0
            listStok = []
            listHarga = []
            for a in file_r:
                i = data_listHstr[line]
                tree.insert('', indek, text='', values=(
                    nomor, i[0], i[1], i[2], i[4]))
                sisa_stok = int(i[3])-int(i[4])
                total_hargaPerbarang = int(i[2])*int(i[4])
                listStok.append(i[0]+'|'+str(sisa_stok)+'|'+i[4])
                listHarga.append(total_hargaPerbarang)
                indek += 1
                line += 1
                nomor += 1
            hsb = ttk.Scrollbar(labelframe)
            hsb.configure(command=tree.yview)
            tree.configure(yscrollcommand=hsb.set)
            hsb.pack(side=RIGHT, fill=Y)
            tree.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

            JumlahTotal = sum(listHarga)
            del listHarga[0:]
            garis = Label(root, text='-'*120,
                          font=('Supermercado One', 13, 'bold'))
            jumlah_total = Label(root, text='Total Harga',
                                 font=('Supermercado One', 13, 'bold'))
            titik_total = Label(root, text=':', font=(
                'Supermercado One', 13, 'bold'))
            rp_total = Label(root, text='Rp.', font=(
                'Supermercado One', 13, 'bold'))
            hasilTotal = Label(root, text=JumlahTotal, font=(
                'Supermercado One', 13, 'bold'))

            garis.place(relx=0.5, rely=0.56, anchor=CENTER)
            jumlah_total.place(relx=0.15, rely=0.64, anchor=CENTER)
            titik_total.place(relx=0.25, rely=0.64, anchor=CENTER)
            rp_total.place(relx=0.30, rely=0.64, anchor=CENTER)
            hasilTotal.place(relx=0.35, rely=0.64, anchor=CENTER)

            #MEMBUAT KODE BAYAR SETELAH SEMUA DATA TELAH DIISI
            def bayar_():
                del total_[0:]
                total_.append(JumlahTotal)
                bayar()

            def bayar():
                for widget in root.winfo_children():
                    widget.destroy()

                header3 = Label(root, text='Menu Pembayaran', font=(
                    'Supermercado One', 15, 'bold'), bg='#CCCCCC')
                l1 = Label(root, text='Total Bayar', font=(
                    'Supermercado One', 13, 'bold'))
                titik_l1 = Label(root, text=':', font=(
                    'Supermercado One', 13, 'bold'))
                rp_l1 = Label(root, text='Rp.', font=(
                    'Supermercado One', 13, 'bold'))
                isi_l1 = Label(root, text=total_[0], font=(
                    'Supermercado One', 13, 'bold'))
                l2 = Label(root, text='Jumlah Uang', font=(
                    'Supermercado One', 13, 'bold'))
                titik_l2 = Label(root, text=':', font=(
                    'Supermercado One', 13, 'bold'))
                rp_l2 = Label(root, text='Rp.', font=(
                    'Supermercado One', 13, 'bold'))
                isi_l2 = Entry(root, textvariable=data3, font=(
                    'Supermercado One', 13, 'bold'), width=10, bg='#CCCCCC')
                isi_l2.delete(0, 'end')
                header3.place(relx=0.5, rely=0.06, anchor=CENTER)
                l1.place(relx=0.4, rely=0.2, anchor=CENTER)
                titik_l1.place(relx=0.5, rely=0.2, anchor=CENTER)
                rp_l1.place(relx=0.55, rely=0.2, anchor=CENTER)
                isi_l1.place(relx=0.6, rely=0.2, anchor=CENTER)
                l2.place(relx=0.4, rely=0.3, anchor=CENTER)
                titik_l2.place(relx=0.5, rely=0.3, anchor=CENTER)
                rp_l2.place(relx=0.55, rely=0.3, anchor=CENTER)
                isi_l2.place(relx=0.64, rely=0.3, anchor=CENTER)

                ##MEMBUAT KODE SUKSES
                def sukses():
                    for widget in root.winfo_children():
                        widget.destroy()
                    uang = data3.get()
                    if uang != '':
                        list_a = []
                        list_a.extend(str(uang.lower()))
                        for p in list_a:
                            if p in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                                bayar()
                                label_err = Label(root, text='(GAGAL) Uang Harus Berupa Angka !!', font=(
                                    'Supermercado One', 8, 'bold'), fg='#d10f0f')
                                label_err.place(
                                    relx=0.5, rely=0.4, anchor=CENTER)
                                break
                        else:
                            if int(total_[0]) <= int(uang):
                                sisaPembayaran = int(uang)-int(total_[0])
                                header4 = Label(root, text='Pembayaran BERHASIL', font=(
                                    'Supermercado One', 15, 'bold'), bg='#1fab34')
                                h1 = Label(root, text='Total Bayar', font=(
                                    'Supermercado One', 13, 'bold'))
                                titik_h1 = Label(root, text=':', font=(
                                    'Supermercado One', 13, 'bold'))
                                rp_h1 = Label(root, text='Rp.', font=(
                                    'Supermercado One', 13, 'bold'))
                                isi_h1 = Label(root, text=total_[0], font=(
                                    'Supermercado One', 13, 'bold'))
                                h2 = Label(root, text='Jumlah Uang', font=(
                                    'Supermercado One', 13, 'bold'))
                                titik_h2 = Label(root, text=':', font=(
                                    'Supermercado One', 13, 'bold'))
                                rp_h2 = Label(root, text='Rp.', font=(
                                    'Supermercado One', 13, 'bold'))
                                isi_h2 = Label(root, text=uang, font=(
                                    'Supermercado One', 13, 'bold'))
                                h3 = Label(root, text='Sisa', font=(
                                    'Supermercado One', 13, 'bold'))
                                titik_h3 = Label(root, text=':', font=(
                                    'Supermercado One', 13, 'bold'))
                                rp_h3 = Label(root, text='Rp.', font=(
                                    'Supermercado One', 13, 'bold'))
                                isi_h3 = Label(root, text=sisaPembayaran, font=(
                                    'Supermercado One', 13, 'bold'))

                                for i in range(len(hstr)):
                                    print(hstr[i], file=open(
                                        'data/historyTransaksi', 'a'))
                                else:
                                    del hstr[0:]

                                line = 1
                                list_a = []
                                for i in listStok:
                                    a = i.split('|')
                                    list_a.append(a)
                                for i in list_a:
                                    kodebarang_ = i[0]
                                    sisastok_ = i[1]
                                    file = open('data/dataBarang',
                                                'r').readlines()
                                    for i in file:
                                        list = []
                                        a = i.replace('\n', '')
                                        a = a.split('|')
                                        list.extend(a)
                                        kodebarang = list[0]
                                        namabarang = list[1]
                                        hargabarang = list[2]
                                        stokbarang = list[3]
                                        if kodebarang_ == kodebarang:
                                            with open('data/dataBarang', 'r') as f:
                                                lines = f.readlines()
                                            with open('data/dataBarang', 'w') as f:
                                                for line in lines:
                                                    if line.strip('') != kodebarang+'|'+namabarang+'|'+hargabarang+'|'+stokbarang+'\n':
                                                        f.write(line)
                                                f.close()
                                            file_ = open(
                                                'data/dataBarang', 'a')
                                            write = kodebarang+'|'+namabarang+'|'+hargabarang+'|'+sisastok_+'\n'
                                            file_.write(write)
                                            file_.close()
                                header4.place(
                                    relx=0.5, rely=0.2, anchor=CENTER)
                                h1.place(relx=0.4, rely=0.35, anchor=CENTER)
                                titik_h1.place(
                                    relx=0.5, rely=0.35, anchor=CENTER)
                                rp_h1.place(relx=0.55, rely=0.35,
                                            anchor=CENTER)
                                isi_h1.place(
                                    relx=0.6, rely=0.35, anchor=CENTER)
                                h2.place(relx=0.4, rely=0.45, anchor=CENTER)
                                titik_h2.place(
                                    relx=0.5, rely=0.45, anchor=CENTER)
                                rp_h2.place(relx=0.55, rely=0.45,
                                            anchor=CENTER)
                                isi_h2.place(
                                    relx=0.6, rely=0.45, anchor=CENTER)
                                h3.place(relx=0.4, rely=0.55, anchor=CENTER)
                                titik_h3.place(
                                    relx=0.5, rely=0.55, anchor=CENTER)
                                rp_h3.place(relx=0.55, rely=0.55,
                                            anchor=CENTER)
                                isi_h3.place(
                                    relx=0.6, rely=0.55, anchor=CENTER)

                                button9 = Button(root, text='Menu Utama', font=(
                                    'Supermercado One', 13, 'bold'), activebackground='#CCCCCC', activeforeground='black', width=10, command=menuUtama, bg='#e9f542')
                                button9.place(
                                    relx=0.5, rely=0.8, anchor=CENTER)

                            elif int(total_[0]) > int(uang):
                                bayar()
                                e1 = Label(root, text='Uang Tidak Cukup Untuk Melanjutkan Pembayaran !!', font=(
                                    'Supermercado One', 8, 'bold'), fg='#e60e19')
                                e1.place(relx=0.5, rely=0.4, anchor=CENTER)
                    else:
                        bayar()
                        err = Label(root, text='Uang Harus Di isi Untuk Melanjutkan Pembayaran !!', font=(
                            'Supermercado One', 8, 'bold'), fg='#e60e19')
                        err.place(relx=0.5, rely=0.4, anchor=CENTER)

                button8 = Button(root, text='Bayar', font=('Supermercado One', 13, 'bold'),
                                 activebackground='#CCCCCC', activeforeground='black', width=10, command=sukses, bg='#74db72')
                Button9 = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                                 activebackground='#CCCCCC', activeforeground='black', width=15, command=menuTransaksi, bg='#e9f542')
                button8.place(relx=0.5, rely=0.5, anchor=CENTER)
                Button9.place(relx=0.5, rely=0.6, anchor=CENTER)

            #MEMBUAT BUTTON UNTUK KEMBALI KE MENU UTAMA
            button6 = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'), activebackground='#CCCCCC',
                             activeforeground='black', width=10, command=menuTransaksi, bg='#e9f542')
            button6.place(relx=0.35, rely=0.82, anchor=CENTER)
            if data_listHstr == []:
                e1 = Label(root, text='Note: Untuk Melanjutkan Pembayaran Minimal ada 1 Barang Dalam Total Keranjang !!', font=(
                    'Supermercado One', 8, 'bold'), fg='#e60e19')
                e1.place(relx=0.5, rely=0.72, anchor=CENTER)
            else:
                button7 = Button(root, text='Bayar', font=('Supermercado One', 13, 'bold'),
                                 activebackground='#CCCCCC', activeforeground='black', width=10, command=bayar_, bg='#74db72')
                button7.place(relx=0.65, rely=0.82, anchor=CENTER)

        button3 = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                         activebackground='#CCCCCC', activeforeground='black', width=10, command=menuUtama, bg='#e9f542')
        button4 = Button(root, text='Keranjang', font=('Supermercado One', 13, 'bold'),
                         activebackground='#CCCCCC', activeforeground='black', width=10, command=Keranjang, bg='#db8472')
        button5 = Button(root, text='Total', font=('Supermercado One', 13, 'bold'),
                         activebackground='#CCCCCC', activeforeground='black', width=10, command=Total, bg='#74db72')

        ktk_namabarang.delete(0, 'end')
        ktk_jmlbarang.delete(0, 'end')
        header2.place(relx=0.5, rely=0.06, anchor=CENTER)
        label_kodebarang.place(relx=0.4, rely=0.2, anchor=CENTER)
        label_jmlbarang.place(relx=0.4, rely=0.3, anchor=CENTER)
        titik_kodebarang.place(relx=0.5, rely=0.2, anchor=CENTER)
        titik_jmlbarang.place(relx=0.5, rely=0.3, anchor=CENTER)
        ktk_namabarang.place(relx=0.6, rely=0.2, anchor=CENTER)
        ktk_jmlbarang.place(relx=0.6, rely=0.3, anchor=CENTER)
        button3.place(relx=0.32, rely=0.5, anchor=CENTER)
        button4.place(relx=0.5, rely=0.5, anchor=CENTER)
        button5.place(relx=0.67, rely=0.5, anchor=CENTER)

    #MEMBUAT BUTTON (MENU ADMIN)
    pin_entered = False  # Variable untuk melacak apakah pin telah dimasukkan
    def menuAdmin():
        for widget in root.winfo_children():
            widget.destroy()
        
        if not pin_entered:
            show_pin_page()
        else:
            show_admin_menu()

    pin_entry = None
    error_label = None

    def validate_pin():
        global pin_entry
        global error_label
        
        entered_pin = pin_entry.get()
        correct_pin = "1234"
        
        if entered_pin == correct_pin:
            show_admin_menu()
        else:
            error_label.config(text="PIN yang Anda masukkan salah")

    def show_pin_page():
        global pin_entry
        global error_label
        
        for widget in root.winfo_children():
            widget.destroy()
        
        pin_label = Label(root, text="Masukkan PIN:", font=('Supermercado One', 15, 'bold'))
        pin_entry = Entry(root, show="*", font=('Supermercado One', 15, 'bold'), width=13)
        submit_button = Button(root, text="Submit", command=validate_pin)
        error_label = Label(root, text="", font=('Supermercado One', 12), fg="red")
        
        pin_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        pin_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        submit_button.place(relx=0.5, rely=0.6, anchor=CENTER)
        error_label.place(relx=0.5, rely=0.7, anchor=CENTER)

    def show_admin_menu():
        for widget in root.winfo_children():
            widget.destroy()
    
        def tambah_db():
            for widget in root.winfo_children():
                widget.destroy()
            
            ##MENAMPILKAN ISI YANG ADA DIDALAM TAMBAH DATA BARANG 
            headerAdmin2 = Label(root, text='Tambah Data Barang', font=(
                'Supermercado One', 15, 'bold'), bg='#CCCCCC')
            p1 = Label(root, text='Kode Barang', font=(
                'Supermercado One', 13, 'bold'))
            p2 = Label(root, text='Nama Barang', font=(
                'Supermercado One', 13, 'bold'))
            p3 = Label(root, text='Harga Barang /pcs',
                       font=('Supermercado One', 13, 'bold'))
            p4 = Label(root, text='Stok Barang', font=(
                'Supermercado One', 13, 'bold'))
            p1_titik = Label(root, text=':', font=(
                'Supermercado One', 13, 'bold'))
            p2_titik = Label(root, text=':', font=(
                'Supermercado One', 13, 'bold'))
            p3_titik = Label(root, text=':', font=(
                'Supermercado One', 13, 'bold'))
            p4_titik = Label(root, text=':', font=(
                'Supermercado One', 13, 'bold'))
            p3_rp = Label(root, text='Rp.', font=(
                'Supermercado One', 13, 'bold'))
            p1_ktk = Entry(root, textvariable=data4, font=(
                'Supermercado One', 13, 'bold'), width=13, bg='#CCCCCC')
            p2_ktk = Entry(root, textvariable=data5, font=(
                'Supermercado One', 13, 'bold'), width=13, bg='#CCCCCC')
            p3_ktk = Entry(root, textvariable=data6, font=(
                'Supermercado One', 13, 'bold'), width=13, bg='#CCCCCC')
            p4_ktk = Entry(root, textvariable=data7, font=(
                'Supermercado One', 13, 'bold'), width=13, bg='#CCCCCC')

            p1_ktk.delete(0, 'end')
            p2_ktk.delete(0, 'end')
            p3_ktk.delete(0, 'end')
            p4_ktk.delete(0, 'end')

            headerAdmin2.place(relx=0.5, rely=0.06, anchor=CENTER)
            p1.place(relx=0.4, rely=0.2, anchor=CENTER)
            p2.place(relx=0.4, rely=0.3, anchor=CENTER)
            p3.place(relx=0.37, rely=0.4, anchor=CENTER)
            p4.place(relx=0.4, rely=0.5, anchor=CENTER)
            p1_titik.place(relx=0.5, rely=0.2, anchor=CENTER)
            p2_titik.place(relx=0.5, rely=0.3, anchor=CENTER)
            p3_titik.place(relx=0.5, rely=0.4, anchor=CENTER)
            p4_titik.place(relx=0.5, rely=0.5, anchor=CENTER)
            p3_rp.place(relx=0.53, rely=0.4, anchor=CENTER)
            p1_ktk.place(relx=0.63, rely=0.2, anchor=CENTER)
            p2_ktk.place(relx=0.63, rely=0.3, anchor=CENTER)
            p3_ktk.place(relx=0.63, rely=0.4, anchor=CENTER)
            p4_ktk.place(relx=0.63, rely=0.5, anchor=CENTER)

            def simpan():
                kode_barang = data4.get()
                nama_barang = data5.get()
                harga_barang = data6.get()
                stok_barang = data7.get()

                file = open('data/dataBarang', 'r').readlines()
                kode = []
                for i in file:
                    list = []
                    a = i.replace('\n', '')
                    a = a.split('|')
                    list.extend(a)
                    kodebarang = list[0]
                    kode.append(kodebarang)
                if str(kode_barang) != '':
                    if str(nama_barang) != '':
                        if str(harga_barang) != '':
                            if str(stok_barang) != '':
                                list_a = []
                                list_a.extend(str(harga_barang.lower()))
                                for p in list_a:
                                    if p in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                                        label_err2 = Label(root, text='(GAGAL) Harga Barang Harus Berupa Angka !!', font=(
                                            'Supermercado One', 8, 'bold'), fg='#d10f0f')
                                        label_err2.place(
                                            relx=0.5, rely=0.6, anchor=CENTER)
                                        break
                                else:
                                    list_b = []
                                    list_b.extend(str(stok_barang.lower()))
                                    for q in list_b:
                                        if q in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                                            label_err2 = Label(root, text='(GAGAL) Stok Barang Harus Berupa Angka !!', font=(
                                                'Supermercado One', 8, 'bold'), fg='#d10f0f')
                                            label_err2.place(
                                                relx=0.5, rely=0.6, anchor=CENTER)
                                            break
                                    else:
                                        if str(kode_barang) not in kode:
                                            new_Barang = kode_barang+'|'+nama_barang+'|'+harga_barang+'|'+stok_barang
                                            print(new_Barang, file=open(
                                                'data/dataBarang', 'a'))
                                            hsAdmin = 'Tambah Data|'+kode_barang + \
                                                '|Menambahkan Data Baru|' + \
                                                waktu(0)
                                            print(hsAdmin, file=open(
                                                'data/historyAdmin', 'a'))
                                            tambah_db()
                                            status = Label(root, text='Data Baru Kode : '+kode_barang+' Berhasil Tersimpan !!', font=(
                                                'Supermercado One', 8, 'bold'), fg='#1fab34')
                                            status.place(
                                                relx=0.5, rely=0.6, anchor=CENTER)
                                        else:
                                            tambah_db()
                                            label_err1 = Label(root, text='(GAGAL) Kode Barang Sudah Terdaftar !!', font=(
                                                'Supermercado One', 8, 'bold'), fg='#d10f0f')
                                            label_err1.place(
                                                relx=0.5, rely=0.6, anchor=CENTER)
                            else:
                                label_err6 = Label(root, text='(GAGAL) Stok Barang Harus diIsi !!', font=(
                                    'Supermercado One', 8, 'bold'), fg='#d10f0f')
                                label_err6.place(
                                    relx=0.5, rely=0.6, anchor=CENTER)
                        else:
                            label_err5 = Label(root, text='(GAGAL) Harga Barang Harus diIsi !!', font=(
                                'Supermercado One', 8, 'bold'), fg='#d10f0f')
                            label_err5.place(relx=0.5, rely=0.6, anchor=CENTER)
                    else:
                        label_err4 = Label(root, text='(GAGAL) Nama Barang Harus diIsi !!', font=(
                            'Supermercado One', 8, 'bold'), fg='#d10f0f')
                        label_err4.place(relx=0.5, rely=0.6, anchor=CENTER)
                else:
                    label_err3 = Label(root, text='(GAGAL) Kode Barang Harus diIsi !!', font=(
                        'Supermercado One', 8, 'bold'), fg='#d10f0f')
                    label_err3.place(relx=0.5, rely=0.6, anchor=CENTER)

            btn_kembali = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                                 activebackground='#CCCCCC', activeforeground='black', width=15, command=show_admin_menu, bg='#e9f542')
            btn_simpan = Button(root, text='Simpan', font=('Supermercado One', 13, 'bold'),
                                activebackground='#CCCCCC', activeforeground='black', width=15, command=simpan, bg='#42c8f5')
            btn_kembali.place(relx=0.35, rely=0.7, anchor=CENTER)
            btn_simpan.place(relx=0.65, rely=0.7, anchor=CENTER)

        #MENAMBAHKAN FUNGSI PADA BUTTON REMOVE BARANG
        def hapus_db():
            for widget in root.winfo_children():
                widget.destroy()

            def lanjut():
                for widget in root.winfo_children():
                    widget.destroy()
                kodebarang_ = data14.get()
                file = open('data/dataBarang', 'r').readlines()
                for i in file:
                    list = []
                    a = i.replace('\n', '')
                    a = a.split('|')
                    list.extend(a)
                    kodebarang = list[0]
                    namabarang = list[1]
                    hargabarang = list[2]
                    stokbarang = list[3]
                    if kodebarang_ == kodebarang:
                        labelframe = LabelFrame(root, text='Hapus Data Barang', font=(
                            'Supermercado One', 15, 'bold'), bg='#CCCCCC')
                        labelframe.grid(column=0, row=0, pady=20,
                                        padx=31, sticky="wens")

                        tree = ttk.Treeview(labelframe, height=4)
                        tree['show'] = 'headings'

                        s = ttk.Style(root)
                        s.theme_use('clam')
                        s.configure("Treeview.Heading", font=(
                            'Supermercado One', 13, 'bold'))
                        s.configure("Treeview", font=(
                            'Supermercado One', 12, 'bold'), rowheight=50)

                        tree['show'] = 'headings'
                        tree['columns'] = ('Jenis', 'Identitas')
                        tree.column('Jenis', width=250,
                                    minwidth=250, anchor=CENTER)
                        tree.column('Identitas', width=450,
                                    minwidth=450, anchor=CENTER)

                        tree.heading('Jenis', text='Jenis', anchor=CENTER)
                        tree.heading(
                            'Identitas', text='Identitas', anchor=CENTER)

                        tree.insert('', 0, text='', values=(
                            'Kode Barang\t\t:', kodebarang))
                        tree.insert('', 1, text='', values=(
                            'Nama Barang\t\t:', namabarang))
                        tree.insert('', 2, text='', values=(
                            'Harga Barang (Rp.)\t :', hargabarang))
                        tree.insert('', 3, text='', values=(
                            'Stok Barang\t\t:', stokbarang))

                        hsb = ttk.Scrollbar(labelframe)
                        hsb.configure(command=tree.yview)
                        tree.configure(yscrollcommand=hsb.set)
                        hsb.pack(side=RIGHT, fill=Y)
                        tree.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

                        lbl_ = Label(root, text='Klik tombol HAPUS untuk Menghapus Data ini ...', font=(
                            'Supermercado One', 10, 'bold'), fg='#3f8feb')
                        lbl_.place(relx=0.5, rely=0.65, anchor=CENTER)

                        def hapus():
                            with open('data/dataBarang', 'r') as f:
                                lines = f.readlines()
                            with open('data/dataBarang', 'w') as f:
                                for line in lines:
                                    if line.strip('') != kodebarang+'|'+namabarang+'|'+hargabarang+'|'+str(stokbarang)+'\n':
                                        f.write(line)
                                f.close()
                            file_ = open('data/dataBarang', 'a')
                            hsAdmin = 'Hapus Data Barang|'+kodebarang + \
                                '|'+'Data Telah Terhapus'+'|'+waktu(0)
                            print(hsAdmin, file=open('data/historyAdmin', 'a'))
                            file_.close()
                            hapus_db()
                            status4 = Label(root, text='Kode Barang : '+kodebarang_+' BERHASIL TERHAPUS !!', font=(
                                'Supermercado One', 8, 'bold'), fg='#1fab34')
                            status4.place(relx=0.5, rely=0.5, anchor=CENTER)

                        btnkembali = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                                            activebackground='#CCCCCC', activeforeground='black', width=15, command=hapus_db, bg='#e9f542')
                        btnhapus = Button(root, text='Hapus', font=('Supermercado One', 13, 'bold'),
                                          activebackground='#CCCCCC', activeforeground='black', width=15, command=hapus, bg='#3f8feb')
                        btnkembali.place(relx=0.38, rely=0.75, anchor=CENTER)
                        btnhapus.place(relx=0.63, rely=0.75, anchor=CENTER)
                        break
                else:
                    hapus_db()
                    label_err2 = Label(root, text='(GAGAL) Kode Barang Tidak Terdaftar !!', font=(
                        'Supermercado One', 8, 'bold'), fg='#d10f0f')
                    label_err2.place(relx=0.5, rely=0.5, anchor=CENTER)

            headerAdmin5 = Label(root, text='Hapus Data Barang', font=(
                'Supermercado One', 15, 'bold'), bg='#CCCCCC')
            a1 = Label(root, text='Kode Barang', font=(
                'Supermercado One', 13, 'bold'))
            a1_titik = Label(root, text=':', font=(
                'Supermercado One', 13, 'bold'))
            a1_ktk = Entry(root, textvariable=data14, font=(
                'Supermercado One', 13, 'bold'), width=13, bg='#CCCCCC')
            a1_ktk.delete(0, 'end')
            a1_btn1 = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                             activebackground='#CCCCCC', activeforeground='black', width=15, command=show_admin_menu, bg='#e9f542')
            a1_btn2 = Button(root, text='Lanjutkan', font=('Supermercado One', 13, 'bold'),
                             activebackground='#CCCCCC', activeforeground='black', width=15, command=lanjut, bg='#42c8f5')

            headerAdmin5.place(relx=0.5, rely=0.2, anchor=CENTER)
            a1.place(relx=0.4, rely=0.4, anchor=CENTER)
            a1_titik.place(relx=0.5, rely=0.4, anchor=CENTER)
            a1_ktk.place(relx=0.6, rely=0.4, anchor=CENTER)
            a1_btn1.place(relx=0.38, rely=0.6, anchor=CENTER)
            a1_btn2.place(relx=0.63, rely=0.6, anchor=CENTER)

        def history():
            for widget in root.winfo_children():
                widget.destroy()
            #MEMBUAT HISTORY TRANSAKSI TUJUAN PEMBELIAN BARANG#
            def historyTransaksi():
                for widget in root.winfo_children():
                    widget.destroy()

                labelframeHstr = LabelFrame(root, text='History Transaksi Pembelian Barang', font=(
                    'Supermercado One', 15, 'bold'), bg='#CCCCCC')
                labelframeHstr.grid(column=0, row=0, pady=20,
                                    padx=20, sticky="wens")

                treeHstr1 = ttk.Treeview(labelframeHstr, height=10)
                treeHstr1['show'] = 'headings'

                s = ttk.Style(root)
                s.theme_use('clam')
                s.configure("Treeview.Heading", font=(
                    'Supermercado One', 13, 'bold'))
                s.configure("Treeview", font=(
                    'Supermercado One', 12, 'bold'), rowheight=25)

                treeHstr1['show'] = 'headings'
                treeHstr1['columns'] = (
                    'No.', 'Kode Barang', 'Nama Barang', 'Jumlah', 'Total Pembelian', 'Waktu')
                treeHstr1.column('No.', width=40, minwidth=40, anchor=CENTER)
                treeHstr1.column('Kode Barang', width=120,
                                 minwidth=120, anchor=CENTER)
                treeHstr1.column('Nama Barang', width=230,
                                 minwidth=230, anchor=CENTER)
                treeHstr1.column('Jumlah', width=70,
                                 minwidth=70, anchor=CENTER)
                treeHstr1.column('Total Pembelian', width=110,
                                 minwidth=110, anchor=CENTER)
                treeHstr1.column('Waktu', width=150,
                                 minwidth=150, anchor=CENTER)

                treeHstr1.heading('No.', text='No.', anchor=CENTER)
                treeHstr1.heading('Kode Barang', text='Kode', anchor=CENTER)
                treeHstr1.heading(
                    'Nama Barang', text='Nama Barang', anchor=CENTER)
                treeHstr1.heading('Jumlah', text='Jumlah', anchor=CENTER)
                treeHstr1.heading('Total Pembelian',
                                  text='Total (Rp.)', anchor=CENTER)
                treeHstr1.heading('Waktu', text='Waktu', anchor=CENTER)

                file = open('data/historyTransaksi', 'r').readlines()
                file_r = open('data/historyTransaksi', 'r').readlines()
                data_listHstr = []
                for i in file:
                    list = []
                    a = i.replace('\n', '')
                    a = a.split('|')
                    list.extend(a)
                    data_listHstr.append(list)
                indek = 0
                nomor = 1
                line = 0
                for a in file_r:
                    i = data_listHstr[line]
                    treeHstr1.insert('', indek, text='', values=(
                        nomor, i[0], i[1], i[2], i[3], i[4]))
                    indek += 1
                    line += 1
                    nomor += 1
                hsbAdmin1 = ttk.Scrollbar(labelframeHstr)
                hsbAdmin1.configure(command=treeHstr1.yview)
                treeHstr1.configure(yscrollcommand=hsbAdmin1.set)
                hsbAdmin1.pack(side=RIGHT, fill=Y)
                treeHstr1.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

                buttonkembali = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                                       activebackground='#CCCCCC', activeforeground='black', width=15, command=history, bg='#e9f542')
                buttonkembali.place(relx=0.5, rely=0.8, anchor=CENTER)
               
                 #//MENAMBAHKAN HISTORY ADMIN///#
            def historyAdmin():
                for widget in root.winfo_children():
                    widget.destroy()

                labelframeAdmn = LabelFrame(root, text='History Admin', font=(
                    'Supermercado One', 15, 'bold'), bg='#CCCCCC')
                labelframeAdmn.grid(column=0, row=0, pady=20,
                                    padx=21, sticky="wens")

                treeAdmn = ttk.Treeview(labelframeAdmn, height=10)
                treeAdmn['show'] = 'headings'

                s = ttk.Style(root)
                s.theme_use('clam')
                s.configure("Treeview.Heading", font=(
                    'Supermercado One', 13, 'bold'))
                s.configure("Treeview", font=(
                    'Supermercado One', 12, 'bold'), rowheight=25)

                treeAdmn['show'] = 'headings'
                treeAdmn['columns'] = (
                    'No.', 'Jenis', 'Kode Barang', 'Perubahan', 'Waktu')
                treeAdmn.column('No.', width=40, minwidth=40, anchor=CENTER)
                treeAdmn.column('Jenis', width=170,
                                minwidth=170, anchor=CENTER)
                treeAdmn.column('Kode Barang', width=110,
                                minwidth=110, anchor=CENTER)
                treeAdmn.column('Perubahan', width=250,
                                minwidth=250, anchor=CENTER)
                treeAdmn.column('Waktu', width=150,
                                minwidth=150, anchor=CENTER)

                treeAdmn.heading('No.', text='No.', anchor=CENTER)
                treeAdmn.heading('Jenis', text='Jenis', anchor=CENTER)
                treeAdmn.heading('Kode Barang', text='Kode', anchor=CENTER)
                treeAdmn.heading('Perubahan', text='Perubahan', anchor=CENTER)
                treeAdmn.heading('Waktu', text='Waktu', anchor=CENTER)

                file = open('data/historyAdmin', 'r').readlines()
                file_r = open('data/historyAdmin', 'r').readlines()
                data_listHstr = []
                for i in file:
                    list = []
                    a = i.replace('\n', '')
                    a = a.split('|')
                    list.extend(a)
                    data_listHstr.append(list)
                indek = 0
                nomor = 1
                line = 0
                for a in file_r:
                    i = data_listHstr[line]
                    treeAdmn.insert('', indek, text='', values=(
                        nomor, i[0], i[1], i[2], i[3]))
                    indek += 1
                    line += 1
                    nomor += 1
                hsbAdmin1 = ttk.Scrollbar(labelframeAdmn)
                hsbAdmin1.configure(command=treeAdmn.yview)
                treeAdmn.configure(yscrollcommand=hsbAdmin1.set)
                hsbAdmin1.pack(side=RIGHT, fill=Y)
                treeAdmn.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

                buttonkembali = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                                       activebackground='#CCCCCC', activeforeground='black', width=15, command=history, bg='#e9f542')
                buttonkembali.place(relx=0.5, rely=0.8, anchor=CENTER)
                
            #///History Program///#
            headerHistory1 = Label(root, text='History Program', font=(
                'Supermercado One', 15, 'bold'), bg='#CCCCCC')
            btnHistory1 = Button(root, text='History Admin', font=('Supermercado One', 13, 'bold'), activebackground='#CCCCCC',
                                 activeforeground='black', width=20, height=4, command=historyAdmin, bg='#42c8f5')
            btnHistory2 = Button(root, text='History Transaksi', font=('Supermercado One', 13, 'bold'), activebackground='#CCCCCC',
                                 activeforeground='black', width=20, height=4, command=historyTransaksi, bg='#74db72')
            btnHistory3 = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                                 activebackground='#CCCCCC', activeforeground='black', width=15, command=show_admin_menu, bg='#e9f542')

            headerHistory1.place(relx=0.5, rely=0.2, anchor=CENTER)
            btnHistory1.place(relx=0.32, rely=0.47, anchor=CENTER)
            btnHistory2.place(relx=0.68, rely=0.47, anchor=CENTER)
            btnHistory3.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        #MENAMBAHKAN SETIAP BUTTON PADA MENU ADMIN#
        headerAdmin1 = Label(root, text='Khusus Admin', font=(
            'Supermercado One', 15, 'bold'), bg='#4CAF50' , fg= 'white')
        buttonAdmin2 = Button(root, text='Tambah Data Barang', font=('Supermercado One', 13, 'bold'),
                              activebackground='#CCCCCC', activeforeground='black', width=20, height=5, command=tambah_db, bg='#4CAF50', fg= 'white')
        buttonAdmin5 = Button(root, text='Remove Barang', font=('Supermercado One', 13, 'bold'),
                              activebackground='#CCCCCC', activeforeground='black', width=20, height=5, command=hapus_db, bg='#9C27B0', fg= 'white')
        buttonAdmin6 = Button(root, text='Riwayat Pembelian', font=('Supermercado One', 13, 'bold'),
                              activebackground='#CCCCCC', activeforeground='black', width=20, height=5, command=history, bg='#FFC107', fg= 'white')
        buttonAdmin7 = Button(root, text='Kembali', font=('Supermercado One', 13, 'bold'),
                              activebackground='#CCCCCC', activeforeground='black', width=15, command=menuUtama, bg='#F44336', fg= 'white')

        headerAdmin1.place(relx=0.5, rely=0.05, anchor=CENTER)
        buttonAdmin2.place(relx=0.5, rely=0.28, anchor=CENTER)
        buttonAdmin5.place(relx=0.2, rely=0.28, anchor=CENTER)
        buttonAdmin6.place(relx=0.8, rely=0.28, anchor=CENTER)
        buttonAdmin7.place(relx=0.5, rely=0.83, anchor=CENTER)

    data1 = StringVar()
    data2 = StringVar()
    data3 = StringVar()
    data4 = StringVar()
    data5 = StringVar()
    data6 = StringVar()
    data7 = StringVar()
    data8 = StringVar()
    data9 = StringVar()
    data10 = StringVar()
    data11 = StringVar()
    data12 = StringVar()
    data13 = StringVar()
    data14 = StringVar()
    #MEMBUAT HEADER DAN JUGA MENU UTAMA KHUSUS ADMIN DAN ORDER DISINI #
    header1 = Label(root, text='TOKO SEMBAKO PRIANGAN 3',
                    font=('Supermercado One', 15, 'bold'), bg='#4CAF50' , fg= 'white')
    button1 = Button(root, text='Khusus Admin', font=('Supermercado One', 13, 'bold'), activebackground='#CCCCCC' , fg= 'white',
                     activeforeground='black', bg='#42c8f5', width=20, height=4, command=menuAdmin)
    button2 = Button(root, text='Order Disini', font=('Supermercado One', 13, 'bold'), activebackground='#CCCCCC',fg= 'white' , 
                     activeforeground='black', bg='#74db72', width=20, height=4, command=menuTransaksi)
    buttonAdmin1 = Button(root, text='Tampilkan Data Barang', font=('Supermercado One', 13, 'bold'),
                      activebackground='#CCCCCC', activeforeground='black', width=20, height=5, command=show_db, bg='#2196F3', fg='white')
    buttonAdmin2 = Button(root, text='Exit', font=('Supermercado One', 13, 'bold'),
                      activebackground='#CCCCCC', activeforeground='black', width=5, height=2, command=exit, bg='#ffae00', fg='white')
    

    header1.place(relx=0.5, rely=0.25, anchor=CENTER)
    button1.place(relx=0.32, rely=0.47, anchor=CENTER)
    button2.place(relx=0.68, rely=0.47, anchor=CENTER)
    buttonAdmin1.place(relx=0.50, rely=0.70, anchor=CENTER)
    buttonAdmin2.place(relx=0.50, rely=0.90, anchor=CENTER)

    os.remove('data/dataKeranjang')
    open('data/dataKeranjang', 'a')

menuUtama()
root.mainloop()