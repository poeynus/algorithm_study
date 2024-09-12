class Solution:
    def isValid(self, s: str) -> bool:
        valid_stack = []
        for i in s:
            if valid_stack > 0:
                if i == ")" and valid_stack[-1] == "(":
                    valid_stack.pop()
                elif i == "]" and valid_stack[-1] == "[":
                    valid_stack.pop()
                elif i == "}" and valid_stack[-1] == "{":
                    valid_stack.pop()
                else:
                    valid_stack.append(i)
            else:
                valid_stack.append(i)
        return not valid_stack


class GPTSolution:
    def isValid(self, s: str) -> bool:
        # 괄호 짝을 딕셔너리로 정의
        pairs = {")": "(", "]": "[", "}": "{"}
        valid_stack = []

        for i in s:
            # 닫힌 괄호일 경우 스택에서 확인
            if i in pairs:
                # 스택이 비어 있지 않고, 스택의 마지막이 해당하는 열린 괄호일 경우 pop
                if valid_stack and valid_stack[-1] == pairs[i]:
                    valid_stack.pop()
                else:
                    return False
            else:
                # 열린 괄호는 스택에 추가
                valid_stack.append(i)

        # 스택이 비어 있으면 모든 괄호가 유효
        return not valid_stack


Solution().isValid("(){}}{")

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

# Input: s = "([])"
# Output: true

# '(', ')', '{', '}', '[', ']'
