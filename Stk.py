stk = [1,2,3,4,5]
print(f"스택의 값 {stk}")
stk.append(6)
print(f"6을 추가한 스택의 값 {stk}")
top_num=stk.pop(-1)
print(f"스택의 탑을 추출한 값{top_num}")
print(f"현재 스택리스트 {stk}")

# 스택의 값 푸쉬 팝 만들고 1. 삽입 2. 삭제 3. 전체 출력 4. 종료 만들기 

stack=[] # 빈 스택 리스트 만든후
top = -1 # 초기의 탑값은 -1이다 아무것도 없을시에 
def push(item):
    global top
    stack.append(item)
    top+=1

def pop():
    global top
    if len(stack) !=0:
        pop_val=stack.pop(len(stack)-1)
       
        top-=1
        return pop_val
    else:
        print("스택의 리스트에 값이 없습니다")
        return None # 스택 리스트에 값이 없기에 논을 반환 
def show():
    print("현재 스택의 값 ",stack)


while __name__ == "__main__":
    num=int(input("1.삽입,2.삭제 3.전체 출력 4. 종료"))
    if num==1:
        push_num=int(input("삽입 할값"))
        push(push_num)
        print("삽입 성공!")
    elif num==2:
        pop_num=pop()
        if pop_num !=None: #이조건식을 쓰는 이유 스택의 값이 비어있으면 None 을 자동으로 반환해기에 논이 아닐경우에 pop_val 값을 리턴받아서 팝넙으로 출력 
            print(f"{pop_num} 인 탑의 값을 삭제를 성공했습니다")
    elif num==3:
        show() # 메인함수에 print() 를쓰는게  더좋다 
    else:
        print("프로그램을 종료합니다")
        break
        

