import sys
import os
import filecmp

def Accepted_Code(in_f, out_f):
    input = in_f.readline
    tmp = sys.stdout
    sys.stdout = out_f
    ##################################################
    # 이 하단에 코드를 입력하세요.

    a, b, c = map(int, input().rstrip().split())
    print(a+b+c)
    
    ##################################################
    sys.stdout = tmp
    return

def Wrong_Answer_Code(in_f, out_f):
    input = in_f.readline
    tmp = sys.stdout
    sys.stdout = out_f
    ##################################################
    # 이 하단에 코드를 입력하세요.

    a, b, c = map(int, input().rstrip().split())
    print(a+b+c)

    ##################################################
    sys.stdout = tmp
    return

input_path = "output_testcase/"
output_path = "result_testcase/"
extension = ".txt"
input_file_name_base = "output_case_"
accepted_output_file_name_base = "_result_by_case_accepted"
wrong_output_file_name_base = "_result_by_case_wrong"
F = 10
T = 1

if not os.path.exists(input_path):
    os.makedirs(input_path)

if not os.path.exists(output_path):
    os.makedirs(output_path)

for i in range(F):
    input_file_name = f'{input_path}{input_file_name_base}{i}{extension}'
    accepted_in_f = open(input_file_name, 'r')
    wrong_in_f = open(input_file_name, 'r')

    accepted_output_file_name = f'{output_path}{i}{accepted_output_file_name_base}{extension}'
    accepted_out_f = open(accepted_output_file_name, 'w')

    wrong_output_file_name = f'{output_path}{i}{wrong_output_file_name_base}{extension}'
    wrong_out_f = open(wrong_output_file_name, 'w')

    for j in range(T):
        Accepted_Code(accepted_in_f, accepted_out_f)
        Wrong_Answer_Code(wrong_in_f, wrong_out_f)

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