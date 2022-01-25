# 한 개의 정수를 입력받아 양수(positive integer)인지 음수(negative number)인지
# 출력하는 작업을 반복하다가 0이 입력되면 종료하는 프로그램을 작성하시오.

while True:
    num = int(input("number? ")) # 정수 입력받기
    if num == 0: # 입력받은 정수가 0일 때 종료
        break;
    elif num > 0: # 양수일 때
        print("positive integer")
    else: # 음수일 때
        print("negative number")