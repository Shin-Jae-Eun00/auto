class Stack:
    '''
    후입선출(LIFO) 방식으로 관리하는 스택 클래스
    '''
    def __init__(self):
        # 스택의 내용을 저장할 리스트
        self.stack_list = []
        # 스택의 최대 크기를 10
        self.max_size = 10

    def push(self, data):
        '''스택에 새로운 데이터를 추가'''
        if len(self.stack_list) >= self.max_size:
            # 10개가 다 채워진 경우 경고 메시지
            print('경고: 스택이 가득 찼습니다. 더 이상 데이터를 추가할 수 없습니다.')
        else:
            self.stack_list.append(data)
            print(f'데이터 \'{data}\' 추가 완료')

    def pop(self):
        '''가장 마지막에 추가된 데이터를 가져오고 삭제'''
        if self.empty():
            # 가져올 내용이 없는 경우 경고 메시지를 출력
            print('경고: 스택이 비어 있어 데이터를 가져올 수 없습니다.')
            return None
        return self.stack_list.pop()

    def empty(self):
        '''스택이 비어 있는지 확인하여 True 또는 False를 반환'''
        return len(self.stack_list) == 0

    def peek(self):
        '''마지막 데이터를 삭제하지 않고 내용 확인'''
        if self.empty():
            print('경고: 스택이 비어 있어 확인할 데이터가 없습니다.')
            return None
        return self.stack_list[-1]

    def visualize(self):
        '''
        스택의 현재 상태를 시각화하여 출력
        '''
        print('\n--- 현재 스택 상태 ---')
        if self.empty():
            print('[ 빈 스택 ]')
        else:
            # 스택의 상단(Top)부터 하단까지 역순으로 출력
            for i in range(len(self.stack_list) - 1, -1, -1):
                if i == len(self.stack_list) - 1:
                    print(f'| {self.stack_list[i]} | <- Top')
                else:
                    print(f'| {self.stack_list[i]} |')
            print('---------------')
        print()


# 과제 수행을 위한 스택 동작 테스트
if __name__ == '__main__':
    # 스택 인스턴스 생성
    mystack = Stack()

    # 1. 데이터 입력 테스트 (고유 번호 포함)
    print('1. 데이터 입력 테스트 시작')
    for i in range(1, 12):  # 11번 반복하여 10개 초과 시 경고 확인
        unique_id = f'ID_{i:02d}'
        mystack.push(unique_id)

    # 2. 상태 시각화
    mystack.visualize()

    # 3. peek 함수 테스트
    top_item = mystack.peek()
    print(f'현재 맨 위의 데이터 확인(peek): {top_item}')

    # 4. 데이터 꺼내기 테스트 (pop)
    print('\n2. 데이터 꺼내기 테스트 시작')
    while not mystack.empty():
        removed_item = mystack.pop()
        print(f'데이터 가져오기(pop): {removed_item}')

    # 5. 비어있는 상태에서 pop 시도 (경고 메시지 확인)
    mystack.pop()

    # 6. 최종 상태 시각화
    mystack.visualize()