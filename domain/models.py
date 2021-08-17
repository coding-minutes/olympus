from dataclasses import dataclass


@dataclass
class Profile:
    first_name: str
    last_name: str
    email: str
    photo: str

    @classmethod
    def from_dict(cls, dikt):
        return cls(
            first_name=dikt.get("given_name") or dikt.get("first_name"),
            last_name=dikt.get("family_name") or dikt.get("last_name"),
            email=dikt.get("email"),
            photo=dikt.get('photo_url'),
        )

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "photo" : self.photo,
        }
