from blockchain import Blockchain
from utils import get_random_string


def main():
    my_blockchain = Blockchain(difficulty=4)

    num_blocks = 3

    for _ in range(num_blocks):
        my_blockchain.add_block(data=get_random_string(10))

    my_blockchain.display_blockchain()

    print("Is chain valid?", my_blockchain.is_chain_valid())


if __name__ == "__main__":
    main()
