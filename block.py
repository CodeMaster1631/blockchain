import hashlib
from datetime import datetime


class Block:
    def __init__(
        self,
        index: int,
        timestamp: float,
        data: str,
        previous_hash: str,
        nonce: int = 0,
        difficulty: int = 4,
    ) -> None:
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.difficulty = difficulty
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}{self.difficulty}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Index: {self.index}\nDate and Time: {datetime.fromtimestamp(self.timestamp)}\nData: {self.data}\nNonce: {self.nonce}\nPrevious Hash: {self.previous_hash}\nCurrent Hash: {self.hash}"
