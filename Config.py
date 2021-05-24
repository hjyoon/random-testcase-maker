# 사용하는 3가지 방법
# 1. 테스트케이스 생성기를 사용하여 만든 입력데이터를 정답코드와 틀린코드에 각각 입력하여 나오는 결과를 비교한다.
# 2. 하나의 고정된 정답을 정하고, 그 정답에 해당하는 테스트케이스를 만들어서 틀린코드에 입력 후, 그 결과를 고정된 정답과 비교한다.
# 3. 테스트케이스 생성기를 사용하지 않고, 입력데이터와 정답데이터를 직접 만든 뒤, 입력데이터를 틀린코드에 입력하여, 그 결과를 정답데이터와 비교한다.

# 입력데이터의 유형
# 1. 테스트케이스의 개수가 입력파일 첫 줄에 명시된 경우와 없는 경우
# 2. 입력데이터의 개수 또는 라인수가 명시된 경우와 없는 경우
# 3. 각 테스트케이스의 끝 줄에 입력데이터의 끝을 명시하는 문자열이 있는 경우와 없는 경우

#=== 공통 ===

# 각 입출력 파일들의 확장자
in_ex = ".in"
out_ex = ".out"

# 테스트케이스 생성기가 생성할 입력케이스 파일의 개수
F = 100

# 테스트케이스 생성기가 생성할 하나의 입력케이스 파일에 들어갈 테스트케이스의 개수
T = 1

#=== TestCaseMaker.py ===

# 테스트케이스 생성기가 생성한 입력케이스를 저장할 경로
output_path_testcase = "generated_testcase/"

# 테스트케이스 생성기가 생성한 입력케이스 파일 앞에 붙는 명칭
output_file_name_base = ""

# 입력케이스 맨 윗줄에 테스트케이스 수를 명시할 경우에 True
WRITE_TESTCASE_IN_A_INPUT = False

# 각 입력케이스의 끝을 알리는 문자열이 존재할 시, 그 문자를 입력케이스 맨 밑줄에 명시할지 여부
WRITE_END_TESTCASE_CH = False

# 모든 테스트케이스가 끝나고 파일의 끝을 알리는 문자열을 맨 밑줄에 명시할지 여부
WRITE_END_FILE_CH = False

#=== TestCode.py ===

# 사용자가 직접 만든 테스트케이스 입력과 출력파일이 저장된 경로
input_path_user_custom = "user_custom_testcase/"

# 데이터를 읽어올 경로
input_path = "generated_testcase/"

# 정답코드와 틀린코드가 출력할 결과가 저장될 경로
output_path_code_result = "result/"

# 생성된 입력케이스 파일 앞에 붙는 명칭
input_file_name_base = ""

# 정답코드가 출력한 결과 파일 뒤에 붙는 명칭
accepted_output_file_name_base = "_ac"

# 틀린코드가 출력한 결과 파일 뒤에 붙는 명칭
wrong_output_file_name_base = "_wa"

# 정답코드와 틀린코드의 결과 비교 시, 정답인 경우 OK출력 여부
SHOW_OK_CASE = True

# 정답코드와 틀린코드의 결과 비교 시, 정답인 경우 입력값 출력 여부
SHOW_OK_CASE_INPUT = False

# 정답코드와 틀린코드의 결과 비교 시, 정답인 경우 결과값 출력 여부
SHOW_OK_CASE_OUTPUT = False

# 정답코드와 틀린코드의 결과 비교 시, 틀린 경우 입력값 출력 여부
SHOW_ERR_CASE_INPUT = True

# 정답코드와 틀린코드의 결과 비교 시, 틀린 경우 결과값 출력 여부
SHOW_ERR_CASE_OUTPUT = True

# 테스트케이스 생성기로부터 생성된 입력파일을 사용하는 모드.
GENERATED_TESTCASE_MODE = 0

# 사용자가 직접 만든 테스트케이스의 입력과 정답을 사용하는 모드.
USER_CUSTOM_MODE = 1

# 어떤 모드를 사용할지 고른다.
TEST_CODE_MODE = USER_CUSTOM_MODE # (GENERATED_TESTCASE_MODE, FIXED_ANSWER_MODE, USER_CUSTOM_MODE) 셋 중 하나를 대입