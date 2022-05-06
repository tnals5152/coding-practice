import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alphabet = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        if s_alphabet == "".join(list(reversed(s_alphabet))):
            return True
        return False
