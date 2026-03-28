class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        answer = ""
        for char in s:
            if char == ']':
                temp = ""
                while stack[-1] != "[":
                    temp += stack.pop()
                bracket = stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = num[::-1]

                for i in range(int(num)):
                    stack.append(temp)
            else:
                stack.append(char)

        for i in range(len(stack)):
            answer += stack[i][::-1]


        return answer


        
