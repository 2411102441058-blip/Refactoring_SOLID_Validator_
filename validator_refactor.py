
from abc import ABC, abstractmethod

class Validator(ABC):
    @abstractmethod
    def validate(self, mahasiswa):
        pass

class SKSValidator(Validator):
    def validate(self, mahasiswa):
        return mahasiswa["sks"] <= 24

class PrasyaratValidator(Validator):
    def validate(self, mahasiswa):
        return mahasiswa["prasyarat"]

class RegistrationValidator:
    def __init__(self, validators):
        self.validators = validators

    def validate(self, mahasiswa):
        for v in self.validators:
            if not v.validate(mahasiswa):
                return "Registrasi gagal"
        return "Registrasi berhasil"

if __name__ == "__main__":
    mahasiswa = {"sks": 20, "prasyarat": True}
    validators = [SKSValidator(), PrasyaratValidator()]
    app = RegistrationValidator(validators)
    print(app.validate(mahasiswa))
