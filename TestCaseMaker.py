import sys
import os
import random
from Config import *

import itertools
import collections

# random.random() # 0이상 1미만 ex) 0.90389642027948769
# random.randrange(1,7) # 1이상 7미만의 난수

# l = [1, 2, 3, 4, 5, 6]
# random.shuffle(l) # 해당 인자의 리스트 원소들을 섞는다
# random.choice(l) # 해당 인자의 리스트 원소 중 하나를 뽑는다

# random.choices(l, k=2) # 리스트 원소를 중복되게 k개 만큼 뽑는다
# random.choices(l, weights=[1,1,1,1,1,1], k=2) # 리스트 원소를 중복되게 k개 만큼 뽑는다. 가중치는 모두 같다
# random.choices(l, cum_weights=[1,2,3,4,5,6], k=2) # 리스트 원소를 중복되게 k개 만큼 뽑는다. 누적가중치를 사용하였으며, 가중치가 모두 같다. [1,1,1,1,1,1] == [1,2,3,4,5,6]

# random.sample(l, 3) # 리스트 원소를 중복되지 않게 k개 만큼 뽑는다
# random.sample(l, counts=[1,1,1,1,1,6], k=5) # 리스트 원소를 중복되지 않게 k개 만큼 뽑는다. counts인자를 통해 각 원소들의 갯수를 정해줄 수 있다.

def each_case():
    N = random.randrange(1,11)
    print(N)
    for _ in range(N):
        a = random.randrange(1,10)
        b = random.randrange(1,10)
        print(a, b)

def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'

if not os.path.exists(output_path_testcase):
    os.makedirs(output_path_testcase)
else:
    removeAllFile(output_path_testcase)

for i in range(1, F+1):
    sys.stdout = open(f'{output_path_testcase}{output_file_name_base}{i:04d}{in_ex}', 'w')
    if WRITE_TESTCASE_IN_A_INPUT:
        print(T)
    for _ in range(T):
        each_case()
        if WRITE_END_TESTCASE_CH:
            print(-1)
    if WRITE_END_FILE_CH:
        print(-1)

    # 파일 마지막 라인의 '\n'를 제거
    sys.stdout.seek(sys.stdout.tell()-2, os.SEEK_SET)
    sys.stdout.truncate()