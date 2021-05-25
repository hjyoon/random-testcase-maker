import sys
import os
from Code_Accepted import Code_Accepted
from Code_Wrong import Code_Wrong
from TestCode_Config import *

def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'

if not os.path.exists(INPUT_PATH_USER_CUSTOM):
    os.makedirs(INPUT_PATH_USER_CUSTOM)

if not os.path.exists(INPUT_PATH_G_TC):
    os.makedirs(INPUT_PATH_G_TC)

if not os.path.exists(OUTPUT_PATH_CODE_RESULT):
    os.makedirs(OUTPUT_PATH_CODE_RESULT)
else:
    removeAllFile(OUTPUT_PATH_CODE_RESULT)

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
        if SHOW_OK_CASE:
            print(f'case #{tc_num}: OK')
            if SHOW_OK_CASE_INPUT:
                print('input:')
                print(*in_l, sep='')
                print()
            if SHOW_OK_CASE_OUTPUT:
                print('accepted:')
                print(*ac, sep='')
                print('wrong answer:')
                print(*wa, sep='')
    else:
        if SHOW_ERR_CASE:
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

if TEST_CODE_MODE == G_TC_MODE:
    for fn in os.listdir(INPUT_PATH_G_TC):
        fn_base, fn_ex = fn.split(".")
        input_file_name = f'{INPUT_PATH_G_TC}{fn_base}{IN_EX}'
        accepted_output_file_name = f'{OUTPUT_PATH_CODE_RESULT}{fn_base}{AC_OUTPUT_FILE_NAME_BASE}{OUT_EX}'
        wrong_output_file_name = f'{OUTPUT_PATH_CODE_RESULT}{fn_base}{WA_OUTPUT_FILE_NAME_BASE}{OUT_EX}'

        run_code(input_file_name, accepted_output_file_name, wrong_output_file_name)
        cmp_ans_proc(fn_base, input_file_name, accepted_output_file_name, wrong_output_file_name)
elif TEST_CODE_MODE == USER_CUSTOM_MODE:
    for fn in os.listdir(INPUT_PATH_USER_CUSTOM):
        fn_base, fn_ex = fn.split(".")
        if fn_ex == OUT_EX:
            continue
        input_file_name = f'{INPUT_PATH_USER_CUSTOM}{fn_base}{IN_EX}'
        accepted_output_file_name = f'{INPUT_PATH_USER_CUSTOM}{fn_base}{OUT_EX}'
        wrong_output_file_name = f'{OUTPUT_PATH_CODE_RESULT}{fn_base}{WA_OUTPUT_FILE_NAME_BASE}{OUT_EX}'

        run_code(input_file_name, accepted_output_file_name, wrong_output_file_name)
        cmp_ans_proc(fn_base, input_file_name, accepted_output_file_name, wrong_output_file_name)