import dataclasses
from datetime import date
from strenum import StrEnum


class Hobby(StrEnum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    gender: str
    phone_number: str
    email: str
    hobbies: list
    current_address: str
    state: str
    city: str
    subject: str
    date_of_birth: date
    photo: str

    @property
    def hobbies_str(self):
        return ', '.join(self.hobbies)


test_user = User(
        first_name='Olga',
        last_name='YA',
        gender='Female',
        phone_number='1234567891',
        email='name@example.com',
        hobbies=[Hobby.SPORTS, Hobby.MUSIC],
        current_address='Moscowskaya Street 18',
        state='NCR',
        city='Delhi',
        subject='Computer Science',
        date_of_birth=date(1999, 5, 11),
        photo='resources/foto.png'
        )
