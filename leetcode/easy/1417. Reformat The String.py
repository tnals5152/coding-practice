import re
class Solution:
    def reformat(self, s: str) -> str:
        alpha_list = list("".join(re.findall('[a-z]+', s)))
        digits_list = list("".join(re.findall('[0-9]+', s)))
        
        if abs(len(alpha_list) - len(digits_list)) >= 2:
            return ""
        else:
            result_str = "".join([*sum(zip(alpha_list, digits_list),())])
            
            if len(alpha_list) != len(digits_list):
                if len(alpha_list) > len(digits_list):
                    return result_str + alpha_list[-1]
                else:
                    return digits_list[-1] + result_str
                
            return result_str
        
