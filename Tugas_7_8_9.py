from Tugas_1_dan_2 import Orang  # type: ignore

class Pelajar(Orang):
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.matkul = []
    
    def enrol(self, matkul):
        self.matkul.append(matkul)

class Pengajar(Orang):
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.matkul_diajar = []
    
    def mengajar(self, matkul_diajar):
        self.matkul_diajar.append(matkul_diajar)

class Asdos(Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        Pelajar.__init__(self, nama_depan, nama_belakang, nomor_ID)
        Pengajar.__init__(self, nama_depan, nama_belakang, nomor_ID)