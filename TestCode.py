import sys
import os
import filecmp
from Code_Accepted import Code_Accepted
from Code_Wrong import Code_Wrong
from Config import *

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
        Code_Accepted()
        sys.stdout = wrong_out_f
        sys.stdin = wrong_in_f
        Code_Wrong()
        sys.stdout = tmp
        sys.stdin = tmp2

    accepted_in_f.close()
    wrong_in_f.close()
    accepted_out_f.close()
    wrong_out_f.close()

    if filecmp.cmp(accepted_output_file_name, wrong_output_file_name):
        if SHOW_OK_CASE:
            print(f'case #{i}: OK')
        pass
    else:
        print(f'case #{i}: ERR')
        if SHOW_ERR_CASE_INPUT:
            input_file_name = f'{input_path}{input_file_name_base}{i}{extension}'
            testcase_in_f = open(input_file_name, 'r')
            print('input:')
            print(*testcase_in_f.readlines(), sep='')
            print()
            testcase_in_f.close()
        if SHOW_ERR_CASE_OUTPUT:
            accepted_out_f = open(accepted_output_file_name, 'r')
            wrong_out_f = open(wrong_output_file_name, 'r')
            print('accepted:')
            print(*accepted_out_f.readlines(), sep='')
            print('wrong answer:')
            print(*wrong_out_f.readlines(), sep='')
            accepted_out_f.close()
            wrong_out_f.close()
        pass