#=== TestCode.py ===

# 정답코드와 틀린코드의 결과 비교 시, 정답인 경우 OK출력 여부
SHOW_OK_CASE = True

# =============== SHOW_OK_CASE == True 인 경우에 사용 ===============

# 정답코드와 틀린코드의 결과 비교 시, 정답인 경우 입력값 출력 여부
SHOW_OK_CASE_INPUT = False

# 정답코드와 틀린코드의 결과 비교 시, 정답인 경우 결과값 출력 여부
SHOW_OK_CASE_OUTPUT = False

# =========================================================================

# 정답코드와 틀린코드의 결과 비교 시, 틀린 경우 ERR출력 여부
SHOW_ERR_CASE = True

# =============== SHOW_ERR_CASE == True 인 경우에 사용 ===============

# 정답코드와 틀린코드의 결과 비교 시, 틀린 경우 입력값 출력 여부
SHOW_ERR_CASE_INPUT = True

# 정답코드와 틀린코드의 결과 비교 시, 틀린 경우 결과값 출력 여부
SHOW_ERR_CASE_OUTPUT = True

# =========================================================================

# 테스트케이스 생성기로부터 생성된 입력파일을 사용하는 모드.
G_TC_MODE = 0

# 사용자가 직접 만든 테스트케이스의 입력과 정답을 사용하는 모드.
USER_CUSTOM_MODE = 1

# 어떤 모드를 사용할지 고른다.
TEST_CODE_MODE = G_TC_MODE # (GENERATED_TESTCASE_MODE, USER_CUSTOM_MODE) 둘 중 하나를 대입

# 사용자 테스트케이스 파일 저장 경로
INPUT_PATH_USER_CUSTOM = "user_custom_testcase/"

# 생성된 테스트케이스 파일 저장 경로
INPUT_PATH_G_TC = "generated_testcase/"

# 정답코드와 틀린코드가 출력할 결과가 저장될 경로
OUTPUT_PATH_CODE_RESULT = "result/"

# 정답코드가 출력한 결과 파일 뒤에 붙는 명칭
AC_OUTPUT_FILE_NAME_BASE = "_ac"

# 틀린코드가 출력한 결과 파일 뒤에 붙는 명칭
WA_OUTPUT_FILE_NAME_BASE = "_wa"

# 각 입출력 파일들의 확장자
IN_EX = ".in"
OUT_EX = ".out"