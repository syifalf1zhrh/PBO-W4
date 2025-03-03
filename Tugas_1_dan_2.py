class Orang :
    def __init__(self, nama_depan, nama_belakang, nomor_ID) :
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_ID = nomor_ID
    
class Mahasiswa(Orang) :
    SARJANA, MAGISTER, DOKTOR = range(3)

    def __init__(self, nama_depan, nama_belakang, nomor_ID, jenjang) :
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, matkul) :
        self.matkul.append(matkul)
