import numpy as np
import sys
import ast

def LCS_numpy(program_code_1, program_code_2): 

    length_program_1 = len(program_code_1) 
    length_program_2 = len(program_code_2) 

    lengths = np.array([[0]*(length_program_2 + 1) for it in range(length_program_1 + 1)])

    for i in range(length_program_1 + 1): 
        for j in range(length_program_2 + 1): 

            if i == 0 or j == 0 : 
                lengths[i][j] = 0

            elif program_code_1[i-1] == program_code_2[j-1]: 
                lengths[i][j] = lengths[i-1][j-1]+1

            else: 
                lengths[i][j] = max(lengths[i-1][j], lengths[i][j-1]) 

    return lengths[length_program_1][length_program_2] 
 
def main():
    with open(sys.argv[1], "r", errors='replace', encoding = "utf8") as file:
        source_string1 = file.read()  

    with open(sys.argv[2], "r", errors='replace', encoding = "utf8") as file:
        source_string2 = file.read() 

    with open(sys.argv[3], "a", encoding = "utf8") as f:
        f.write("\nThe length of the longest commnon substring of " + sys.argv[1] + " " + sys.argv[2] + " is equal to " + str(LCS_numpy(source_string1, source_string2)))
        
if __name__ == '__main__':
    main()
