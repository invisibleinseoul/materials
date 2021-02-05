# + 에 대하여 설명을 드립니다.
a=6
b=3
c=7

#a*b=ab -> 컴퓨터에서 인식 못합니다.
# / -> 몫과 나머지를 실수 형태로 나타냄
# // -> 몫만 나타냄
# % -> 나머지만 나타냄
# ** -> 제곱 연산, **의 왼쪽은 밑수, **의 오른쪽은 지수


#list - [],list()
#데이터 생성, 삭제, 수정, 읽기,삽입
asdf=[1,2,3,4,5,"apple"] #list 생성 -데이터 생성
    # 0 1 2 3 4 5 -> 자료의 인덱스
print(asdf)  # list 읽기-데이터 읽기
asdf.append(6)
asdf.append("banana")
#데이터 삭제 remove, del (delete약자) , pop
print(asdf)
# asdf=[2,3,4,5,"apple",6]
      # 0 1 2 3 4 5
asdf.remove("banana")
del asdf[0]
del asdf[4]
del asdf[asdf.index(3)]
print(asdf)
asdf.pop(0)
print(asdf)

# 리스의 요소를 수정하고 싶을 때
asdf[2]=8
print(asdf)

#리스트 나타내는 기호 - list()
bear=list()
groot=list((1,2,3))  #(1,2,3)- tuple
#print(bear ,groot)

# dict  : 왼쪽은 key : 의 오른쪽은 value
adobe={"apple":"사과",'banana':"바나나",'orange':"오렌지"}
print(adobe)
#dict 자료를 추가하고 싶다 -> update 
adobe.update({"아보카도":"avocado","딸기":'strawberry'})
print(adobe)
#dict 자료를 직접적으로 추가
adobe['망고']="mango"
adobe['사과']="사과는 사과야"
print(adobe)
#dict에 있는 자료를 확인하고 싶을 때

print(adobe.keys())
print(adobe.values())
print(adobe.items())



adobe={"apple":"사과",'banana':"바나나",'orange':"오렌지"}
print(adobe)
for i in adobe:
    print(i)
