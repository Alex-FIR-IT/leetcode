class Solution:
    def removeStars(self, string_: str) -> str:
        symbols = []

        for symbol in string_:
            if symbol == '*':
                symbols.pop()
            else:
                symbols.append(symbol)

        return ''.join(symbols)
    