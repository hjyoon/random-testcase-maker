import sys
import os
import filecmp

def Accepted_Code():
    import math
    n,*l=map(int,sys.stdin)
    l=sorted(l[:n])
    l=[w-v for v,w in zip(l,l[1:])]
    g=math.gcd(*l)
    print(sum(i//g-1 for i in l))
    pass

def Wrong_Answer_Code():
    import math

    _, *S = map(lambda x:int(x.rstrip()), sys.stdin)
    S = sorted(S[:_])
    t=[b-a for a,b in zip(S,S[1:])]

    r = math.gcd(*t)
    print(sum(t)//r-len(t))
    pass

input_path = "output_testcase/"
output_path = "result_testcase/"
extension = ".txt"
input_file_name_base = "output_case_"
accepted_output_file_name_base = "_result_by_case_accepted"
wrong_output_file_name_base = "_result_by_case_wrong"
F = 1000
T = 1

if not os.path.exists(input_path):
    os.makedirs(input_path)

if not os.path.exists(output_path):
    os.makedirs(output_path)

for i in range(1, F+1):
    input_file_name = f'{input_path}{input_file_name_base}{i}{extension}'
    accepted_in_f = open(input_file_name, 'r')
    wrong_in_f = open(input_file_name, 'r')

    accepted_output_file_name = f'{output_path}{i}{accepted_output_file_name_base}{extension}'
    accepted_out_f = open(accepted_output_file_name, 'w')

    wrong_output_file_name = f'{output_path}{i}{wrong_output_file_name_base}{extension}'
    wrong_out_f = open(wrong_output_file_name, 'w')

    for j in range(T):
        tmp = sys.stdout
        tmp2 = sys.stdin
        sys.stdout = accepted_out_f
        sys.stdin = accepted_in_f
        Accepted_Code()
        sys.stdout = wrong_out_f
        sys.stdin = wrong_in_f
        Wrong_Answer_Code()
        sys.stdout = tmp
        sys.stdin = tmp2

    accepted_in_f.close()
    wrong_in_f.close()
    accepted_out_f.close()
    wrong_out_f.close()

    if filecmp.cmp(accepted_output_file_name, wrong_output_file_name):
        print(f'case #{i}: OK')
    else:
        accepted_out_f = open(accepted_output_file_name, 'r')
        wrong_out_f = open(wrong_output_file_name, 'r')
        print(f'case #{i}: ERR')
        print('accepted:')
        print(*accepted_out_f.readlines(), sep='')
        print('wrong answer:')
        print(*wrong_out_f.readlines(), sep='')
        accepted_out_f.close()
        wrong_out_f.close()