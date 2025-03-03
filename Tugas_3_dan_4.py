from Tugas_1_dan_2 import Orang # type: ignore
class  Karyawan(Orang):
    TETAP, TDK_TETAP = range(2)

    def __init__(self, nama_depan, nama_belakang, nomor_ID, status):
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.status = status

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_ID, stastus):
        super().__init__(nama_depan, nama_belakang, nomor_ID, stastus)
        self.matkul_diajar = []

    def mengajar(self, matkul_diajar):
        self.matkul_diajar.append(matkul_diajar)

# Contoh objek
if __name__ == "__main__":
    karyawan1 = Karyawan("Budi", "Santoso", "12345", Karyawan.TETAP)
    dosen1 = Dosen("Siti", "Aisyah", "67890", Karyawan.TETAP)
    
    dosen1.mengajar("Matematika")
    dosen1.mengajar("Fisika")
    
    print(f"Karyawan: {karyawan1.nama_depan} {karyawan1.nama_belakang}, ID: {karyawan1.nomor_ID}, Status: {karyawan1.status}")
    print(f"Dosen: {dosen1.nama_depan} {dosen1.nama_belakang}, ID: {dosen1.nomor_ID}, Status: {dosen1.status}, Mata Kuliah: {', '.join(dosen1.matkul_diajar)}")
