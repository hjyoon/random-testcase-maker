import sys
import os
from TestCaseMaker_Config import *
from Each_Case import Each_Case

def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'

if not os.path.exists(OUTPUT_PATH_TC):
    os.makedirs(OUTPUT_PATH_TC)
else:
    removeAllFile(OUTPUT_PATH_TC)

if TC_MAKER_MODE == MANY_FILE_TC_MODE:
    for i in range(1, T+1):
        sys.stdout = open(f'{OUTPUT_PATH_TC}{i:04d}{IN_EX}', 'w')
        Each_Case()
        if WRITE_END_FILE_CH:
            print(END_FILE_CH)
        # 파일 마지막 라인의 '\n'를 제거
        sys.stdout.seek(sys.stdout.tell()-2, os.SEEK_SET)
        sys.stdout.truncate()
elif TC_MAKER_MODE == ONE_FILE_TC_MODE:
    sys.stdout = open(f'{OUTPUT_PATH_TC}{1:04d}{IN_EX}', 'w')
    if WRITE_TC_IN_A_INPUT:
        print(T)
    for _ in range(T):
        Each_Case()
        if WRITE_END_TC_CH:
            print(END_TC_CH)
    if WRITE_END_FILE_CH:
        print(END_FILE_CH)
    # 파일 마지막 라인의 '\n'를 제거
    sys.stdout.seek(sys.stdout.tell()-2, os.SEEK_SET)
    sys.stdout.truncate()