
class ValidatorManager:
    def validate(self, mahasiswa):
        if mahasiswa["sks"] > 24:
            return "SKS melebihi batas"
        elif not mahasiswa["prasyarat"]:
            return "Prasyarat belum terpenuhi"
        else:
            return "Registrasi berhasil"

if __name__ == "__main__":
    mahasiswa = {"sks": 20, "prasyarat": True}
    app = ValidatorManager()
    print(app.validate(mahasiswa))
