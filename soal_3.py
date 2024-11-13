jumlah_barang = int(input('Masukkan jumlah barang')) 
total_belanjaan = 0
for x in range(jumlah_barang):
    print(f'masukkan nilai ke-{x}') 
    nilai =float (input(f'masukkan Harga barang ke-{i -1}: '))
    total_belanjaan+=nilai
    
print(f'Total belanjaan : Rp. {total_belanjaan:.2f}')
