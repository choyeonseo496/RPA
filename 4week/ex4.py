def sumfunc(num):
    sum = 0
    for j in range(1, num+1) :
        sum=sum+j
        return sum
    
    sum = sumfunc(num)
    print(f"1~{num}까지 정수의 합은 {sum} 입니다.")