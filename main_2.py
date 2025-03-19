from blockchain import Blockchain


def main():
    data = input("Enter data for the block: ")

    my_blockchain = Blockchain(difficulty=4)

    my_blockchain.add_block(data)
    my_blockchain.display_blockchain()
    my_blockchain.is_chain_valid()


if __name__ == "__main__":
    main()
