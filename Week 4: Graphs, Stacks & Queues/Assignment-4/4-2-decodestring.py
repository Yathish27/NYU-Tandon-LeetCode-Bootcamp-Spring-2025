class Solution:
    def decodeString(self, s: str) -> str:
        def decode(position):
            result = ''
            number = 0
            while position < len(s):
                char = s[position]
                
                if char.isdigit():
                    number = number * 10 + int(char)
                    
                elif char == '[':
                    nested_str, new_pos = decode(position + 1)
                    result += nested_str * number
                    number = 0
                    position = new_pos
                elif char == ']':
                    return result, position
                    
                else:
                    result += char
                
                position += 1
            return result, position
        decoded_string, _ = decode(0)
        return decoded_string
