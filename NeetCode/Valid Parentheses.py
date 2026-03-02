class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "[" or char == "{" or char == "(":
                stack.append(char)

            elif char == "]":
                if stack:
                    if stack[-1] != "[":
                        return False
                    stack.pop()
                else:
                    return False
                
            elif char == "}":
                if stack:
                    if stack[-1] != "{":
                        return False
                    stack.pop()
                else:
                    return False
            else:
                if stack:
                    if stack[-1] != "(":
                        return False
                    stack.pop()
                else:
                    return False
                
        return True if not stack else False

if __name__ == "__main__":
    print(Solution().isValid("({[]})"))