import sys
origin_result = open(sys.argv[1], "r")
digits = origin_result.read()

import re
digits = re.sub("SAT\\n","",digits)
digits = re.sub("0\\n","",digits)
digits = re.sub(r"-[0-9]*","",digits)
digits = digits.split()

digits = list(map(int, digits))

ans = open("final_answer.txt", "w")
for i in range(1, 9):
    for j in range(1, 9):
        if j == (digits[i-1]%10):
            ans.write("o" + " ")
        else:
            ans.write("x" + " ")
    ans.write("\n")

origin_result.close()
