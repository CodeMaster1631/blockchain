import random

users: list[str] = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Heidi",
    "Ivan",
    "Judy",
    "Mallory",
    "Oscar",
    "Peggy",
    "Walter",
    "Zara",
    "Victor",
    "Trent",
    "Mimi",
    "Nancy",
    "Olivia",
    "Peter",
    "Quincy",
    "Rachel",
    "Steve",
]

miners = [
    "Alice",
    "Bob",
    "Charlie",
]


def get_random_user() -> str:
    return random.choice(users)


def get_random_amount() -> float:
    return round(random.uniform(0.1, 100.0), 4)


def get_random_miner() -> str:
    return random.choice(miners)


class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float, message: str = ""):
        self._sender = sender
        self._receiver = receiver
        self._amount = amount
        self._message = message

    @property
    def sender(self) -> str:
        return self._sender

    @property
    def receiver(self) -> str:
        return self._receiver

    def __str__(self) -> dict[str, str]:
        return {
            "sender": self._sender,
            "receiver": self._receiver,
            "amount": self._amount,
        }


def get_transaction() -> Transaction:
    sender = get_random_user()
    receiver = get_random_user()
    while sender == receiver:
        receiver = get_random_user()
    amount = get_random_amount()
    message = f"{sender} paid {amount} to {receiver}"
    return Transaction(sender, receiver, amount, message)


def get_random_string(length: int) -> str:
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length))