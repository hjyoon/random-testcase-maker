# 여러개의 파일로 이루어진 테스트케이스 모드
MANY_FILE_TC_MODE = 0

# 하나의 파일 안에 여러 테스트케이스가 포함된 모드
ONE_FILE_TC_MODE = 1

# 어떤 모드를 사용할지 고른다.
TC_MAKER_MODE = MANY_FILE_TC_MODE # (MANY_FILE_TESTCASE_MODE, ONE_FILE_TESTCASE_MODE) 둘 중 하나를 대입

# 생성할 테스트케이스 개수 (1 ~ 9999)
T = 20

# 생성된 테스트케이스 파일 저장 경로
OUTPUT_PATH_TC = "generated_testcase/"

# 모든 테스트케이스가 끝나고 파일의 끝을 알리는 문자열을 맨 밑줄에 명시할지 여부
WRITE_END_FILE_CH = False

# =============== WRITE_END_FILE_CH == True 인 경우에 사용 ===============

# 파일의 끝을 알리는 문자열을 지정
END_FILE_CH = '-1'

# =========================================================================

# =============== ONE_FILE_TESTCASE_MODE 모드를 사용 할 경우 ===============

# 파일의 맨 윗 줄에 테스트케이스 수를 명시할 경우에 True
WRITE_TC_IN_A_INPUT = True

# 각 테스트케이스 끝을 알리는 문자열이 존재할 시, 그 문자를 테스트케이스 맨 밑 줄에 명시할지 여부
WRITE_END_TC_CH = False

# =============== WRITE_END_TESTCASE_CH == True 인 경우에 사용 ===============

# 테스트케이스 끝을 알리는 문자열을 지정
END_TC_CH = '-1'

# =========================================================================

# =========================================================================

# 각 입출력 파일들의 확장자
IN_EX = ".in"
OUT_EX = ".out"