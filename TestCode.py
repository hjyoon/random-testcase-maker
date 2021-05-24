import sys
import os
from Code_Accepted import Code_Accepted
from Code_Wrong import Code_Wrong
from Config import *

def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'

if not os.path.exists(input_path_user_custom):
    os.makedirs(input_path_user_custom)

if not os.path.exists(input_path):
    os.makedirs(input_path)

if not os.path.exists(output_path_code_result):
    os.makedirs(output_path_code_result)
else:
    removeAllFile(output_path_code_result)

def run_code(input_file_name, accepted_output_file_name, wrong_output_file_name):
    tmp, tmp2 = sys.stdout, sys.stdin

    sys.stdout = open(accepted_output_file_name, 'w')
    sys.stdin = open(input_file_name, 'r')
    Code_Accepted()
    sys.stdout.close()

    sys.stdout = open(wrong_output_file_name, 'w')
    sys.stdin.seek(0, os.SEEK_SET)
    Code_Wrong()
    sys.stdout.close()

    sys.stdin.close()

    sys.stdout, sys.stdin = tmp, tmp2

def cmp_ans_proc(tc_num, input_name, ac_f_name_1, wa_f_name_2):
    in_l = open(input_name, 'r').readlines()
    ac = open(ac_f_name_1, 'r').readlines()
    wa = open(wa_f_name_2, 'r').readlines()
    if ac == wa:
        print(f'case #{tc_num}: OK')
    else:
        print(f'case #{tc_num}: ERR')
        if SHOW_ERR_CASE_INPUT:
            print('input:')
            print(*in_l, sep='')
            print()
        if SHOW_ERR_CASE_OUTPUT:
            print('accepted:')
            print(*ac, sep='')
            print('wrong answer:')
            print(*wa, sep='')

if TEST_CODE_MODE == GENERATED_TESTCASE_MODE:
    for fn in os.listdir(input_path):
        fn_base, fn_extension = fn.split(".")
        input_file_name = f'{input_path}{fn}'
        accepted_output_file_name = f'{output_path_code_result}{fn_base}{accepted_output_file_name_base}{out_ex}'
        wrong_output_file_name = f'{output_path_code_result}{fn_base}{wrong_output_file_name_base}{out_ex}'

        run_code(input_file_name, accepted_output_file_name, wrong_output_file_name)
        cmp_ans_proc(fn_base, input_file_name, accepted_output_file_name, wrong_output_file_name)
elif TEST_CODE_MODE == USER_CUSTOM_MODE:
    for fn in os.listdir(input_path_user_custom):
        fn_base, fn_extension = fn.split(".")
        if fn_extension == out_ex:
            continue
        input_file_name = f'{input_path_user_custom}{fn_base}{in_ex}'
        accepted_output_file_name = f'{input_path_user_custom}{fn_base}{out_ex}'
        wrong_output_file_name = f'{output_path_code_result}{fn_base}{wrong_output_file_name_base}{out_ex}'

        run_code(input_file_name, accepted_output_file_name, wrong_output_file_name)
        cmp_ans_proc(fn_base, input_file_name, accepted_output_file_name, wrong_output_file_name)