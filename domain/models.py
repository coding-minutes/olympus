from dataclasses import dataclass


@dataclass
class Profile:
    first_name: str
    last_name: str
    email: str
    photo: str
    id: str

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "photo": self.photo,
            "id": self.id,
        }
