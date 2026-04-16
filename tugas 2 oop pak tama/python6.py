inventaris = {
"Pensil": 10,
"Buku": 3,
"Penghapus": 1,
"Pulpen": 4
}
print("Barang dengan stok rendah:")
for barang, stok in inventaris.items():
   if stok < 5:
     print(barang, "- stok:", stok)