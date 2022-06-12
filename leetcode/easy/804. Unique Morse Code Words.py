class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result_set = set()
        
        letter_dict = {
             "a": ".-",
             "b": "-...",
             "c": "-.-.",
             "d": "-..",
             "e": ".",
             "f": "..-.",
             "g" : "--.",
             "h": "....",
             "i": "..",
             "j": ".---",
             "k": "-.-",
             "l": ".-..",
             "m": "--",
             "n": "-.",
             "o": "---",
             "p": ".--.",
             "q": "--.-",
             "r": ".-.",
             "s": "...",
             "t": "-",
             "u": "..-",
             "v": "...-",
             "w": ".--",
             "x": "-..-",
             "y": "-.--",
             "z": "--.."
        }
        
        for word in words:
            code = ""
            for w in word:
                code += letter_dict[w]
            
            result_set.add(code)
            
        return len(result_set)
