class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for i in tokens:
            if i == "+":
                numbers.append(numbers.pop() + numbers.pop())
            elif i == "-":
                a,b = numbers.pop(), numbers.pop()
                numbers.append(b - a)
            elif i == "*":
                numbers.append(numbers.pop() * numbers.pop())
            elif i == "/":
                a,b = numbers.pop(), numbers.pop()
                numbers.append(int(float(b)/a))
            else:
                numbers.append(int(i))
        return int(numbers[-1])