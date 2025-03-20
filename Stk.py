''' # 여러줄 주석
stk = [10,20,30]
print(f"기존값 : {stk}")# 파이썬은 프린트 형식이면서 f string 형식 
stk.append(40) # append 함수 추가한다. 
print(f"40 추가 후 결과 = {stk}") #top 스택의 꼭대기
# topNum = stk.pop() 꺼내는 함수 리스트에서 Pop 함수 
topNum = stk.pop(-1) # 스택에 -1번에 값을 가져와라 파이썬 맨왼쪽 -1이라 하면 맨 마지막 인덱스 주소 
print("topNum=%d" % topNum) # %d 정수형 형식 지정자 들어감 topNum=40 출력 형식을 확실하게 구별하기 위함함
print("topNum=" ,topNum) #이래도 나옴 topNum=40 이런식 둘다 같음 
print(f"40삭제후 결과 ={stk}")
'''
def push(item) : # 함수를 만듬 push 탭키 자동으로 들어감
    global top
    stack.append(item) 
    top += 1   #top= top+1 지역변수!#! 

def pop():
    global top #global 함수 선언을 해줘야한다
    if len(stack) !=0 : #len(stack) 스택의 길이 !0 0과 같지않으면 참참 if문 안 들여쓰기 
        #num = stack.pop()
        #num = stack.pop(-1)
        #num = stack.pop(len(stack) -1)
        num = stack.pop(-1) #스택의 마지막ㄱ 원소값 삭제. 
        top -= 1  
        return num
    else:
        print("stack 이 텅 비어서 pop 불가함")

stack= [] #리스트 방식의 텅 빈 스택을 선언 한다.
top = -1 
 # 언더바 name 파이썬에서 만든거 패키지나 모듈이름이 구별하기 위한 변수이다 __name__
if __name__ == "__main__": 
    while True :
        num = int(input("1:삽입,2:삭제,3:종료 중,4 전체 출력 선택= ")) #문자열 input, int(input("1:삽입"))
        if num == 1:
            val = int(input("삽입할 데이터="))
            push(val)
            print("stack=", stack)
        elif num == 2: #파이썬은 elif 자바랑 다름
            pop_val = pop()
            if pop_val != None:
                print("stack의 top값 = %d" % pop_val)
                print("stack=", stack)
        else:
            print("3 종료를 입력하였습니다.")
            break
       

          
