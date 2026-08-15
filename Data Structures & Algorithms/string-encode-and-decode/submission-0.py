class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_string = ''
        for s in strs:
            enc_string += str(len(s)) + '#' + s
        return enc_string

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1:j + 1 + length]
            decoded.append(word)
            i = j + 1 + length

        return decoded
