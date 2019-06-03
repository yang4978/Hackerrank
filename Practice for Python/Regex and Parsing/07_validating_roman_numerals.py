#https://www.hackerrank.com/challenges/validate-a-roman-number/problem

#regex_pattern = r"^C?M{0,3}(CM)?C?D?X?C{0,3}X?L?I?X{0,3}I?V?I{0,3}$"	# Do not delete 'r'.
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))
