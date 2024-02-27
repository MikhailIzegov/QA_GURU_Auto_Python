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


test_user = User('Olga', 'YA', 'Female', '1234567891', 'name@example.com', 'Reading',
                 'Moscowskaya Street 18', 'NCR', 'Delhi', 'Computer Science')
