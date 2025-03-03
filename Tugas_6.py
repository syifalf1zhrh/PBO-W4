from Tugas_3_dan_4 import Dosen  # type: ignore

#objek tugas 6

dsn= Dosen("Rizki", "Setiabudi", "456789", Dosen.TETAP)
dsn.mengajar("Statistik")

print(f"\nNama Dosen: {dsn.nama_depan} {dsn.nama_belakang}")
print(f"Nomor ID: {dsn.nomor_ID}")
print(f"Status: {dsn.status}")
print(f"Mengajar: {', '.join(dsn.matkul_diajar)}")