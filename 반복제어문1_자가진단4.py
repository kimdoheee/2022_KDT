# 정수를 계속 입력받다가 100 이상의 수가 입력이 되면 마지막 입력된 수를 포함하여
# 합계와 평균을 출력하는 프로그램을 작성하시오.
# (평균은 반올림하여 소수 첫째자리까지 출력한다.)

total = 0
cnt = 0
while True:
    num = int(input("정수 입력 :")) # 정수 입력받기
    if num >= 100:
        total += num
        cnt += 1
        print("합계 :", total)
        print("평균 : %.1f" % (total/cnt))
        break;

    else:
        total += num
        cnt += 1
