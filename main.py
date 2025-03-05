from blockchain import Blockchain
from utils import get_transaction


def main():
    my_blockchain = Blockchain(4)

    num_blocks = 3

    for _ in range(num_blocks):
        transactions = generate_transactions(3)
        my_blockchain.add_block(transactions)

    # my_blockchain.balances["Alice"] = 100
    # my_blockchain.balances["Bob"] = 50

    # transactions = [
    # {"from": "Alice", "to": "Bob", "amount": 10},
    # {"from": "Bob", "to": "Alice", "amount": 5}
    # ]

    # my_blockchain.add_block("Miner1", transactions)
    my_blockchain.display_blockchain()
    print("Balances:", my_blockchain.balances)


def generate_transactions(n: int = 3) -> list:
    transactions: list[str] = []

    for _ in range(n):
        transactions.append(get_transaction().__str__())

    return transactions


if __name__ == "__main__":
    main()
