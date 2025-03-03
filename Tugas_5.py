from Tugas_1_dan_2 import Mahasiswa # type: ignore

#objek Tugas 5

mhs= Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
mhs.enrol("Basis Data")

print (f"\nNama: {mhs.nama_depan} {mhs.nama_belakang}")
print (f"Nomor ID: {mhs.nomor_ID}")
print (f"Jenjang: {mhs.jenjang}")
print(f"Mata Kuliah yang diambil: {', '.join(mhs.matkul)}")