from blockchain import Blockchain
from utils import get_transaction


def main():
    my_blockchain = Blockchain(difficulty=4)

    num_blocks = 3

    for _ in range(num_blocks):
        transactions = generate_transactions(3)
        my_blockchain.add_block(transactions)

    my_blockchain.display_blockchain()

    print("Is chain valid?", my_blockchain.is_chain_valid())


def generate_transactions(n: int = 3) -> list:
    transactions: list[str] = []

    for _ in range(n):
        transactions.append(get_transaction().__str__())

    return transactions


if __name__ == "__main__":
    main()
