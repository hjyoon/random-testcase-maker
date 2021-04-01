import os
import random

# random.random() # 0이상 1미만 ex) 0.90389642027948769

# random.randrange(1,7) # 1이상 7미만의 난수

# l = [1, 2, 3, 4, 5, 6]
# random.shuffle(l) # 해당 인자의 리스트 원소들을 섞는다

# l = ['a', 'b', 'c', 'd']
# random.choice(l) # 해당 인자의 리스트 원소 중 하나를 뽑는다

output_path = "output_testcase/";
output_file_name_base = "output_case_";
extension = ".txt";
F = 100
T = 1

# 폴더가 존재하지 않을 경우, 폴더를 생성
if not os.path.exists(output_path):
    os.makedirs(output_path)

for i in range(F):
    f = open(f'{output_path}{output_file_name_base}{i}{extension}', 'w')
    for j in range(T):
        a = random.randrange(1,5)
        b = random.randrange(1,5)
        c = random.randrange(1,5)
        f.write(f'{a} {b} {c}')
    f.close()