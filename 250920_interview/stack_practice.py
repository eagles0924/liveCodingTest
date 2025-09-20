

"""
edge case
- 닫는 괄호가 제일 처음에 들어오는 경우
고려해야할 경우
- pair가 안맞는 경우
- stack에 아직 남아있는데 끝난 경우
"""
lst = '(}'
pair = {')': '(', ']': '[', '}': '{'}
closed = [')', ']', '}']

def check(lst):
    stack = []
    # 닫는 괄호 먼저 들어오는 경우
    cnt = -1
    for thing in lst:
        cnt += 1
        if not stack and thing in closed:
            return False
        
        if thing not in pair.keys():
            stack.append(thing)
        
        else:
            if pair[thing] != stack.pop():
                return False
    
    return not stack

# pair = {'(': ')', '[': ']', '{': '}'}
# print('(' in pair.keys())

print(check(lst))