import time
from block import Block
import psycopg


class Blockchain:
    skip_genesis: bool = False
    db_params = {
        "dbname": "postgres",
        "user": "postgres",
        "password": "postgres",
        "host": "localhost",
        "port": "5432",
    }

    def __init__(self, difficulty: int = 4, skip_genesis=False):
        self.chain: list[Block] = []
        self.difficulty = difficulty
        try:
            self.fetch_blocks_from_db()
        except Exception as e:
            print(f"Error fetching blocks from DB: {e}")
            self.create_blockchain_in_db()
            if not skip_genesis:
                Blockchain.skip_genesis = True
                self.create_genesis_block()

    def create_genesis_block(self) -> None:
        genesis_block = Block(
            1, time.time(), "Genesis Block", "0", difficulty=self.difficulty
        )
        self.chain.append(genesis_block)
        self.save_block_to_db(genesis_block)

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: str) -> bool:
        prev_block = self.get_latest_block()
        new_block = Block(
            len(self.chain) + 1,  # Corrected index
            time.time(),
            data,
            prev_block.hash,
            difficulty=self.difficulty,
        )
        self.mine_block(new_block)
        self.chain.append(new_block)
        self.save_block_to_db(new_block)
        return True

    def mine_block(self, block: Block) -> None:
        while not block.hash.startswith("0" * block.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()

    def display_blockchain(self) -> None:
        print("-" * 50)
        for block in self.chain:
            print(block)
            print("-" * 50)

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                print(f"Invalid hash at block {current_block.index}")
                return False

            if current_block.previous_hash != prev_block.hash:
                print(f"Invalid previous hash at block {current_block.index}")
                return False

        return True

    def save_block_to_db(self, block: Block) -> None:
        try:
            with psycopg.connect(**self.db_params) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO blockchain (timestamp, data, previous_hash, hash, nonce) VALUES (%s, %s, %s, %s, %s)",
                        (
                            block.timestamp,
                            block.data,
                            block.previous_hash,
                            block.hash,
                            block.nonce,
                        ),
                    )
                conn.commit()
        except Exception as e:
            print(f"Error saving block to DB: {e}")

    def fetch_blocks_from_db(self) -> None:
        try:
            with psycopg.connect(**self.db_params) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM blockchain ORDER BY index ASC")
                    rows = cur.fetchall()

                if not rows:
                    print("No blockchain found in the database")
                    return

                for row in rows:
                    index, timestamp, data, previous_hash, hash, nonce = row
                    block = Block(index, timestamp, data, previous_hash, difficulty=self.difficulty)
                    block.hash = hash  # Restore the hash from the database
                    block.nonce = nonce  # Restore the nonce from the database
                    self.chain.append(block)
        except Exception as e:
            print(f"Error fetching blocks from DB: {e}")
            raise

    def create_blockchain_in_db(self):
        try:
            with psycopg.connect(**self.db_params) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        CREATE TABLE IF NOT EXISTS blockchain (
                            index SERIAL PRIMARY KEY, 
                            timestamp REAL, 
                            data TEXT, 
                            previous_hash TEXT, 
                            hash TEXT, 
                            nonce INT
                        )
                        """
                    )
                conn.commit()
        except Exception as e:
            print(f"Error creating blockchain in DB: {e}")