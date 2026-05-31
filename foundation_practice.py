# # print(5)
# # print(-10)
# # print(3.14)
# # print(1000)
# # print(5+3)
# # print(2*8)
# # print(3*(3+1))

# # #문자형
# # print('풍선')
# # print("나비")
# # print("z" * 9)


# # #Boolean
# # print(5 > 10)
# # print(5 < 10)
# # print(True)
# # print(False)
# # print(not True)
# # print(not (5 > 10))


# # #변수
# # animal = "고양이"
# # name = "뤈냥이"
# # age = 2
# # hobby = "낮잠"
# # is_adult = (age >= 3)


# # '''이렇게 하면 ]됩니다ㅎㅎㅎㅎㅎㅎㅎㅎ'''


# # print("우리집 " + animal + "의 이름은 " + name + "에요")
# # print(name, "는 "+ str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# # print(name + "는 어른일까요? " + str(is_adult))

# # #quiz
# # station = "사당"
# # station2 = "신도림"
# # station3 = "인천공항"

# # print(station + "행 열차가 들어오고 있습니다.")
# # print(station2 + "행 열차가 들어오고 있습니다.")
# # print(station3 + "행 열차가 들어오고 있습니다.")


# # #연산자
# # print(1+1)
# # print(6/2)

# # print(2**3) #2^3
# # print(5%3) #나머지
# # print(5//3) #몫

# # print(10 > 3)
# # print(4 >= 7)

# # print(3 == 3) #똑같은지 확인하는 연산
# # print(3 == 4)
# # print(3+4 == 7)
# # print(1 != 3) #같지 않다는 뜻
# # # print(not(1 != 3))
# # print((3 > 0) and (3 > 5))
# # print((3 > 0) & (3 < 5))

# # print((3 > 0) or (3 > 5))
# # # print((3 > 0) | (3 > 5))


# # # print(5 > 4 > 3)
# # # print(5 > 4 > 7)


# # print(2 + 3 * 4)
# # print((2 + 3) * 4)
# # number = 2 + 3 * 4
# # print(number)

# # number = number + 2
# # print(number)

# # number += 2
# # print(number)

# # number *= 2
# # print(number)

# # number /= 2
# # print(number)

# # number -= 2
# # print(number)

# # number %= 5
# # print(number)


# # print(abs(-5))

# # print(pow(4, 2)) #4^2

# # print(max(5, 12)) #12
# # print(min(5, 12)) #5
# # print(round(3.14)) #3
# # print(round(4.99)) #5

# # from math import *
# # print(floor(4.99))
# # print(ceil(3.14))
# # print(sqrt(16)) #4


# # from random import *
# # print(random()) #0.0이상, 1.0 미만의 임의의 값 생성
# # print(random() * 10)
# # print(int(random() * 10))
# # print(int(random() * 10))
# # print(int(random() * 10))

# # from random import *
# # print(int(random() * 45) + 1)
# # print(int(random() * 45) + 1)

# # randint(1, 28) #1, 28 포함 사이 아무 숫자
# # print(randrange(1, 46)) #1~46미만의 값 생성

# # from random import *
# # date = randrange(4, 29)
# # print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# # sentence = '난 소년'
# # print(sentence)
# # sentence2 = "파이썬은 쉬워" 
# # print(sentence2)
# # setence3 = """
# # 나는 소년,
# # 파이썬 쉽다
# # """

# # #slicing
# # jumin = "050521-3213333"

# # print("성별 : " + jumin[7])
# # print("연 : " + jumin[0:2])
# # print("월 : " + jumin[2:4])
# # print("일 : " + jumin[4:6])

# # print("생년월일 : " + jumin[:6])
# # print("뒤 7자리 : " + jumin[7:])
# # print("뒤 7자리 : " + jumin[-7:]) #맨 뒤 7번째부터 끝까지


# # python = "Python is Amazing"
# # print(python.lower())
# # print(python.upper())
# # print(python[0].isupper())
# # print(python[0].islower())

# # print(len(python))
# # print(python.replace("Python" , "Java"))

# # index = python.index("n")
# # print(index)

# # index = python.index("n", index + 1)
# # print(index)

# # print(python.find("n"))
# # print(python.count("n"))


# # print("a" + "b")
# # print("a", "b")

# # # 방법 1
# # print("나는 %d살입니다." % 20)
# # print("나는 %s을 좋아해요." % "파이썬")
# # print("Apple 은 %c로 시작해요." % "A")

# # print("나는 %s색과 %s색을 좋아해요." % ("파란" , "빨간"))

# # 방법 2
# # print("나는 {}살입니다.".format(20))
# # print("나는 {}색과 {}색을 좋아해요.".format("파란" , "빨간"))
# # print("나는 {1}색과 {0}색을 좋아해요.".format("파란" , "빨간"))
# # print("나는 {0}색과 {1}색을 좋아해요.".format("파란" , "빨간"))

# # 방법 3
# # print("나는 {age}살이고 {color}색을 좋아해요.".format(age = 20 , color = "빨간"))

# # 방법 4
# # age = 20
# # color = "빨간"
# # print(f"나는 {age}살이고 {color}색을 좋아해요.")


# # print("백문이 붙여일견\n백견이 불여일타")
# # print("나는 \"이현진\"입니다.")

# # \\ : 문장 내에서 \로 바뀜
# # print("\\Users\\")

# # #\r : 커서를 맨 앞으로 이동
# # print("Red Apple\rPine")


# # 리스트 []

# # #지하철 칸별로 10명, 20명, 30명
# # subway = [10, 20, 30]
# # print(subway)

# # subway = ["유재석" , "조세호" , "박명수"]
# # print(subway)

# # print(subway.index("조세호"))

# # #하하씨가 담 정류장에서 탐
# # subway.append("하하")
# # print(subway)

# # #정형돈을 유재석 조세호 사이에 넣기
# # # subway.insert(1, "정형돈")
# # # print(subway)

# # # #한명씩 뒤에서 빼기
# # # print(subway.pop())
# # # print(subway)

# # subway.append("유재석")
# # print(subway)
# # print(subway.count("유재석"))


# # #정렬
# # num_list = [5, 2, 4, 3, 1]
# # num_list.sort()
# # print(num_list)

# # #순서 뒤집기
# # num_list.reverse()
# # print(num_list)

# # #지우기
# # num_list.clear()
# # print(num_list)

# # mix_list = ["조세호" , 20, True]
# # num_list = [5, 2, 4, 3, 1]
# # num_list.extend(mix_list)
# # print(num_list)


# # cabinet = {3: "유재석" , 100: "조세호"}
# # print(cabinet[3])

# # print(cabinet.get(100))

# # print(3 in cabinet)
# # print(7 in cabinet)

# # cabinet[6] = "김진짜"
# # cabinet[3] = "여진구"

# # print(cabinet)

# # del cabinet[3]
# # print(cabinet)

# # print(cabinet.keys())
# # print(cabinet.values())
# # print(cabinet.items())

# # cabinet.clear()
# # print(cabinet)

# # 튜플
# # menu = ("돈까스" , "치즈까스")
# # print(menu[0])

# # name = "김종국"
# # age = 20
# # hobby = "코딩"

# # print(name, age, hobby)

# # (name, age, hobby) = ("김종국", 20, "코딩")

# # print(name, age, hobby)



# # 세트: 중복 O 순서 X
# # my_set = {1,2,3,3,3}
# # print(my_set)

# # java = {"유재석" , "김태호" , "조세호"}
# # python = set(["유재석" , "박명수"])

# # #교집합
# # print(java & python)
# # print(java.intersection(python))

# # #합집합
# # print(java | python)
# # print(java.union(python))


# # #차집합
# # print(java - python)
# # print(java.difference(python))


# # #add
# # python.add("양세형")
# # print(python)

# # #if statements
# # weather = input("날씨? ")
# # if weather == "비" | weather = "눈": 
# #     print("우산을 챙기세요")
# # elif weather == "미세먼지" : 
# #     print("마스크")
# # else:
# #     print("준비물 없음")

# # temp = int(input("기온? "))
# # if 30 <= temp:
# #     print("개더움")
# # elif 10<= temp & temp < 30:
# #     print("날씨 굳")
# # elif 0 <= temp and temp < 10:
# #     print("아우터")
# # else:
# #     print("개추움")

# # for
# # for waiting_no in [0, 1, 2, 3, 4]:
# #     print("대기번호 : {0}".format(waiting_no))

# # for waiting_no in range(1, 6):
# #     print("대기번호 : " + str(waiting_no))


# # starbucks = ["아이언맨" , "토르" , "그루트"]
# # for customer in starbucks:
# #     print(customer + " 커피 나옴")

# # while
# # customer = "토르"
# # index = 5
# # while index >= 1:
# #     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
# #     index -= 1
# #     if index == 0:
# #         print("커피 없음.")

# # continue & break
# # absent = [2, 5]
# # for student in range(1, 11):
# #     if student in absent:
# #         continue
# #     print("{0}번, 책 읽어".format(student))

# # students = [1, 2, 3, 4, 5]
# # print(students)
# # students = [i+100 for i in students]
# # print(students)

# # students = ["Iron man" , "Thor" , "I am Groot"]
# # students = [len(i) for i in students]
# # print(students)

# # students = students = ["Iron man" , "Thor" , "I am Groot"]
# # students = [i.upper() for i in students]
# # print(students)

# # function
# # def open_account():
# #     print("새로운 계좌가 생성되었습니다")

# # open_account()

# # def deposit(balance, money):
# #     print("입금이 완료되었다. 잔얙은 {0} 원.".format(balance + money))
# #     return balance + money

# # balance = 0
# # balance = deposit(balance, 1000)
# # print(balance)


# # 지역변수 전역변수
# # gun = 10
# # def checkpoint(soldiers):
# #     global gun
# #     gun = gun - soldiers
# #     print("[함수 내] 남은 총: {0}".format(gun))

# # print("전체 총: " + gun)
# # checkpoint(2)
# # print("남은 총: " + gun)

# # import sys
# # print("Python" , "Java" , "Javascript" , file = sys.stdout)
# # print("Python" , "Java" , "Javascript" , file = sys.stderr)

# # scores = {"수학":0, "영어":50, "코딩":100}
# # for subject, score in scores.items():
# #     print(subject, score)

# #파일 입출력
# # score_file = open("score.txt" , "w" , encoding = "utf8")
# # print("수학 : 0" , file = score_file)
# # print("영어 : 50" , file = score_file)
# # score_file.close()

# # score_file = open("score.txt" , "a" , encoding = "utf8")
# # score_file.write("과학 : 80")
# # score_file.write("\n코딩 : 100")
# # score_file.close()

# # score_file = open("score.txt" , "r" , encoding="utf8")
# # print(score_file.read())
# # score_file.close()

# # score_file = open("score.txt" , "r" , encoding="utf8")
# # print(score_file.readline()) #줄 별로 읽기 
# # print(score_file.readline())
# # print(score_file.readline())
# # print(score_file.readline())
# # score_file.close()

# # score_file = open("score.txt" , "r" , encoding="utf8")
# # while True:
# #     line = score_file.readline()
# #     if not line: 
# #         break
# #     print(line)
# # score_file.close()

# #피클
# # import pickle
# # # profile_file = open("profile.pickle" , "wb")
# # # profile = {"이름":"박명수" , "나이":30 , "취미":["축구" , "골프" , "코딩"]}
# # # print(profile)
# # # pickle.dump(profile, profile_file)
# # # profile_file.close()

# # # profile_file = open("profile.pickle" , "rb")
# # # profile = pickle.load(profile_file)
# # # print(profile)
# # # profile_file.close

# # with open("profile.pickle" , "rb") as profile_file:
# #     print(pickle.load(profile_file))

# #클래스
# class Unit: 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)
# # marine3 = Unit("마린", 40, 5)

# # wraith1 = Unit("레이스" , 80 , 5)

# #메소드
# # class AttackUnit:
# #     def __init__(self, name, hp, damage):
# #         self.name = name
# #         self.hp = hp
# #         self.damage = damage
    
# #     def attack(self, location):
# #         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

# #     def damaged(self, damage):
# #         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
# #         self.hp -= damage
# #         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
# #         if self.hp <= 0:
# #             print("{0} : 파괴되었습니다.".format(self.name))

# # firebat1 = AttackUnit("파이어뱃" , 50, 16)
# # firebat1.attack("5시")

# # firebat1.damaged(25)
# # firebat1.damaged(25)


# #모듈






