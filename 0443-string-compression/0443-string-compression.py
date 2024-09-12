class Solution:
    def compress(self, chars: List[str]) -> int:

        end = 0
        index = 0

        while end < len(chars):

            current_char = chars[end]
            count = 0

            while end < len(chars) and chars[end] == current_char:
                end += 1
                count += 1

            chars[index] = current_char
            index += 1

            if count > 1:
                for x in str(count):

                    chars[index] = x
                    index += 1

        return index
