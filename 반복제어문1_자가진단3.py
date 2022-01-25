# 한 개의 정수를 입력받아 양수(positive integer)인지 음수(negative number)인지
# 출력하는 작업을 반복하다가 0이 입력되면 종료하는 프로그램을 작성하시오.

while True:
    num = int(input("number? "))
    if num == 0:
        break;
    elif num > 0:
        print("positive integer")
    else:
        print("negative number")