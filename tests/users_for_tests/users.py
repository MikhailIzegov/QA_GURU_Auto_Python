import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    gender: str
    phone_number: str
    email: str
    hobby: str
    current_address: str
    state: str
    city: str
    subject: str


test_user = User(
        first_name='Olga',
        last_name='YA',
        gender='Female',
        phone_number='1234567891',
        email='name@example.com',
        hobby='Reading',
        current_address='Moscowskaya Street 18',
        state='NCR',
        city='Delhi',
        subject='Computer Science'
        )
