# 개요

[BOJ](https://www.acmicpc.net/) 에서 문제를 풀다가 테스트케이스가 필요한 경우가 많았는데, 테스트케이스를 자동으로 만들어주는 프로그램이 있으면 어떨까 싶어서 제가 직접 만들어 보았습니다.

또한, 정답 코드와 틀린 코드를 비교해서 어떤 테스트케이스의 결과가 다른지 확인할 수 있는 코드의 결과 값 검사기도 만들어 보았습니다.

## 목차

1. [구성](#구성)
2. [소스 리스트](#소스-리스트)
3. [사용법](#사용법)

## 구성

- 랜덤 테스트케이스 생성기
- 테스트케이스를 사용한 자동 코드 검사기

## 소스 리스트

### 랜덤 테스트케이스 생성기

| 소스 | 설명 |
|---|---|
| Each_Case.py | 각각의 테스트케이스 데이터를 지정하는 코드 |
| TestCaseMaker.py | 전체 테스트케이스 데이터를 생성하는 메인 코드 |
| TestCaseMaker_Config.py | 데이터 생성을 위한 여러가지 옵션이 들어있는 코드 |

### 테스트케이스를 사용한 자동 코드 검사기

| 소스 | 설명 |
|---|---|
| TestCode.py | 전체 코드 검사를 수행하는 메인 코드 |
| Code_Accepted.py | 정답 코드 |
| Code_Wrong.py | 틀린 코드 |
| TestCode_Config.py | 코드 검사 옵션이 들어있는 코드 |

## 사용법

### 랜덤 테스트케이스 생성기

1. Each_Case.py 에서 하나의 테스트케이스를 작성한다.
2. TestCaseMaker_Config.py 에서 옵션을 설정한다.
3. TestCaseMaker.py 를 실행하면 옵션에 지정된 경로에 ".in" 파일이 생성된다

### 테스트케이스를 사용한 자동 코드 검사기

1. Code_Accepted.py 의 Code_Accepted 함수 내에 정답 코드를 넣는다.
2. Code_Wrong.py 의 Code_Wrong 함수 내에 틀린 코드를 넣는다.
3. TestCode_Config.py 에서 옵션을 설정한다.
4. TestCode_Config.py 실행한다.