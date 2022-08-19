'''
Question 1: DNA String Computations Part 1
View Past Answers
No past answers.
Consider the problem of comparing DNA sequences. A DNA sequence consists of a string
where every character is one of the following 4 letters: ‘A’, ‘C’, ‘G’, or ‘T’. For example, a
DNA sequence might be the string “TCCTATTCTT”.

First we would like to know what the Hamming distance is between several DNA sequences. The Hamming distance between two strings of 
equal length is the number of positions at which the corresponding characters are different.

For example, the Hamming distance between “ATCGT” and “CTAGG” is 3 because the two strings have different characters at 3 positions, 
namely positions 0, 2, and 4. If there are more than 2 input strings, the Hamming distance needs to be computed between any pair of two 
strings. For example, given 3 input strings, the Hamming distance is computed between the 1st and the 2nd, the 1st and the 3rd as well as the 
2nd and the 3rd strings.

Your Task:

Implement the function:
def hamming_distances(dna_str_list)

This takes as input a list of DNA strings dna_str_list and returns a list of integers containing the Hamming distances among all pairs of 
strings, dist_list. Do not change the function name and the parameters or else the autograder will have problems testing the code and you 
will not pass this question.

The return value dist_list should contain the Hamming distances in the following order: string pair
1st and 2nd, string pair 1st and 3rd, string pair 1st and 4th, …, string pair 1st and Nth, string pair 2nd and 3rd, string pair 2nd and 4th, 
…, string pair 2nd and Nth, etc., until string pair N-1th and Nth.

In case of different-length input sequences, the program should return “Strings are of unequal length.”

You may assume that all DNA strings are given in capitalized form and their lengths are at least 1.
'''
def hamming_distances(dna_str_list):
    lengths = list(map(lambda x: len(x), dna_str_list))
    if max(lengths) != min(lengths):
        return  "Strings are of unequal length."
    elif 0 in lengths:
        return 0

    def processor(str1, str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count

    def recursion(dna_str_list):
        if not dna_str_list:
            return [] 
        else:
            return [processor(dna_str_list[0], x) for x in dna_str_list[1:]] + recursion(dna_str_list[1:])
    
    return recursion(dna_str_list)

print(hamming_distances(['ATTCC', 'CCATT']))
print(hamming_distances(['AATCCCGT', 'TCCAACGT', 'CGTAATCC']))
print(hamming_distances(['CCATTGCC', 'ATGCCGCC', 'ATTGCCCC', 'TTACCCGT']))
print(hamming_distances(['ATTCCGT', 'ACCTGA']))

'''
Question 2: DNA STRING COMPUTATIONS PART 2
View Past Answers
No past answers.
Second, we would like to know whether the given DNA sequences are rotations of each other. A DNA sequence (let’s call it DNA2) 
is a rotation of another sequence (say DNA1) if it can be produced by shifting the letters of the DNA1 sequence either to the 
left or to the right while the characters wrap around at the beginning or the end of the string.

As an example, the following illustration shows a rotation where the second string “TTAGC” is a rotation of the original sequence “CTTAG” 
(the string was shifted to the left by one position and the first character was moved to the end).

Your Task:

Implement the function check_rotations(dna_str_list) which takes in a list of DNA strings and returns a list of 0's and 1's. 
For each DNA string, if it has a rotation in the input DNA list, the result for that DNA is 1. Otherwise, result is 0. The input and 
output list should have the same length.

Do not change the function name and the parameters or else the autograder will have problems testing the code and you will not pass this question.

In case of different-length input sequences, the program should print “Strings are of unequal length.”

You may assume that all DNA strings are given in capitalized form and their lengths are at least 1.
'''
def check_rotations(dna_str_list):
    lengths = list(map(lambda x: len(x), dna_str_list))
    if max(lengths) != min(lengths):
        return  "Strings are of unequal length."
    elif 0 in lengths:
        return 0

    def processor(str1, str2):
        if str1 in str2*3:
            return True
        else:
            return False

    copy_list = [0 for i in dna_str_list]
    def recursion(dna_str_list):
        if not dna_str_list:
            return [] 
        else:
            for x in dna_str_list[1:]:
                if copy_list[dna_str_list.index(dna_str_list[0])] == 1:
                    break
                if processor(dna_str_list[0], x):
                    copy_list[dna_str_list.index(dna_str_list[0])] = 1
                    copy_list[dna_str_list.index(x)] = 1

            return recursion(dna_str_list[1:])

    recursion(dna_str_list)
    return copy_list
print(check_rotations(['ATTCC', 'CCATT']))
print(check_rotations(['AATCCCGT', 'TCCAACGT', 'CGTAATCC']))
print(check_rotations(['CCATTGCC', 'ATGCCGCC', 'ATTGCCCC', 'TTACCCGT']))
print(check_rotations(['ATTCCGT', 'ACCTGA']))
