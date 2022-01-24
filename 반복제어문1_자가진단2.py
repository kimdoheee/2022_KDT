# 100 이하의 양의 정수만 입력된다.
# while 문을 이용하여 1부터 입력받은 정수까지의 합을 구하여 출력하는 프로그램을 작성하시오.

num = int(input()) # num 입력하기
i = 0 # 변수 초기화
total = 0 # 총합계 변수 초기화
while i <= num:
    if num <= 100:
        total += i # num 1 부터 total 변수에 저장
        i += 1 # num 1씩 증가

    else:
        print("100 이하의 숫자를 입력해주세요")
        break;
print(total)

