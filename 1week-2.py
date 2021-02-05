#set 자료형 알아보기
#set이라고 꼭 써주기
a=set([1,2,3])
print(a)
b=set([4,5,6])
print(b)
#set의 원소 추가
a.add(4)
print(a)
a.update([2,3,4,5])
print(a)
a.remove(3)
a.discard(5)
print(a)
#집합 a 와 집합 b 를 교집합
print(a.intersection(b))
print(a&b)

#집합 a 와 집합 b 를 합집합
print(a.union(b))
print(a|b)

#집합 a 와 집합 b 를 차집합
print(a.difference(b)) 


#tuple에 대하여 알아봅시다.
#tuple 자료의 수정 안되요. 한번 생성하면 끝
c=tuple((1,2))
d=(3,4)
print(c)
print(d)

#문자열 자료형에 대하여 알아봅시다.
#str 자료형
trax="문자열은 이렇게 생성합니다."
     # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
     #                   . . .  -3  -2  -1
ring='작은 따옴표로 생성하셔도 됩니다.'
num=str(123456789)

#문자열은 리스트랑 치환이 가능합니다.
print(trax*3)

#문자열 슬라이싱 
#
print(trax[:3])
print(trax[3:])
print(trax[3:-3])
print(trax[-3:])
print(num[:4]) # 끝나는 부분은 인덱스 +1 
print(num[-5:])

#boolean 자료형
# 0 이 False 인지 True 인지 알아보자.
print(bool(0))
print(bool(1))
print(bool(12))
l=[1,2,3]
dict1={'사과':'apple'}
print(bool(l))
print(bool(dict1))

#bool 사용하기 위해서 if 문
# == -> 같다. , = -> 대입 , != -> 같지 않다
number=[2,4,5,3,6,4,7,6,8,9,12]

for n in number:
    if n%3==0:
        print(str(n)+"이 3의 배수")
    else:
        print(str(n)+"이 3의 배수 아님")

if 10%2==1:   # if - 조건문 (true) 이 때 실행
    print("홀수")
else:
    print("짝수")


# for문의 다른 종류

for i in range(10):
    print(i)

# for 문의 range 와 문자열 합치기
for i in range(len(num)): #len -> 길이를 의미 length약자 len(trax)->trax문자열의 길이
    print(num[i])