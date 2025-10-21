from typing import List


class PlayfairCipher:

    def __init__(self, key: str):
        self._alphabets = [chr(i) for i in range(ord('A'), ord('Z') + 1) if chr(i) != 'J']
        self.matrix = [[""] * 5 for _ in range(5)]
        self.key = self._prepare_text(key.upper().replace("J", "I"))
        self._mapping = dict()
        self._initialize_matrix()

    def _prepare_text(self, text: str) -> str:
        """
        Prepare string by removing spaces, replacing J with I, and removing duplicates in key.
        """
        result = []
        seen = set()
        for char in text:
            if char not in seen and char in self._alphabets:
                seen.add(char)
                result.append(char)
        return "".join(result)

    def _initialize_matrix(self):
        i, j = 0, 0
        # Add key characters first
        for char in self.key:
            if char in self._alphabets:
                self._alphabets.remove(char)
                self.matrix[i][j] = char
                self._mapping[char] = (i, j)
                if j == 4:
                    i += 1
                    j = 0
                else:
                    j += 1

        # Add remaining alphabets
        for char in self._alphabets:
            if i == 5:
                break
            self.matrix[i][j] = char
            self._mapping[char] = (i, j)
            if j == 4:
                i += 1
                j = 0
            else:
                j += 1

    def _remove_duplicates(self, text: str) -> List[str]:
        """
        Splits text into pairs and separate duplicates inserting 'X'.
        Replace 'J' with 'I' as per Playfair rules.
        """
        text = text.upper().replace("J", "I").replace(" ", "")
        res = []
        i = 0
        while i < len(text):
            char1 = text[i]
            if i + 1 == len(text):
                # Padding for odd length
                res.append(char1 + 'X')
                i += 1
            else:
                char2 = text[i + 1]
                if char1 == char2:
                    # Insert X between duplicates
                    res.append(char1 + 'X')
                    i += 1
                else:
                    res.append(char1 + char2)
                    i += 2
        return res

    def _get_replacement(self, text: str, encrypt: bool = True) -> str:
        """
        Get replaced characters for a digraph according to Playfair cipher rules.
        `encrypt` controls direction of shifting.
        """
        char1, char2 = text[0], text[1]
        (r1, c1), (r2, c2) = self._mapping[char1], self._mapping[char2]

        if r1 == r2:  # Same row
            if encrypt:
                c1 = (c1 + 1) % 5
                c2 = (c2 + 1) % 5
            else:
                c1 = (c1 - 1) % 5
                c2 = (c2 - 1) % 5

            return self.matrix[r1][c1] + self.matrix[r2][c2]

        elif c1 == c2:  # Same column
            if encrypt:
                r1 = (r1 + 1) % 5
                r2 = (r2 + 1) % 5
            else:
                r1 = (r1 - 1) % 5
                r2 = (r2 - 1) % 5

            return self.matrix[r1][c1] + self.matrix[r2][c2]

        else:
            # Rectangle swap
            return self.matrix[r1][c2] + self.matrix[r2][c1]

    def encrypt(self, text: str) -> str:
        pairs = self._remove_duplicates(text)
        res = []
        for p in pairs:
            res.append(self._get_replacement(p, encrypt=True))
        return "".join(res)

    def decrypt(self, text: str) -> str:
        # text must be passed as concatenated encrypted digraphs (no spaces)
        if len(text) % 2 != 0:
            raise ValueError("Encrypted text length must be even")
        pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
        res = []
        for p in pairs:
            res.append(self._get_replacement(p, encrypt=False))
        return "".join(res)


if __name__ == "__main__":
    obj1 = PlayfairCipher(key="MONARCHY")
    encrypted = obj1.encrypt("Hello World")
    print(f"Encrypted: {encrypted}")  # Encrypted text without spaces
    decrypted = obj1.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")  # Should print "HELXLOWORLD" (X inserted between doubles or as padding)
    # Matrix and mapping for debugging
    print("Matrix:")
    for row in obj1.matrix:
        print(row)
    print("Mapping:", obj1._mapping)
