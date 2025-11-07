    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def apply_operator(operands, operator):
    b = operands.pop()
    a = operands.pop()
    if operator == '+':
        operands.push(a + b)
    elif operator == '-':
        operands.push(a - b)
    elif operator == '*':
        operands.push(a * b)
    elif operator == '/':
        operands.push(a / b)

def evaluate_expression(expression):
    operands = Stack()
    operators = Stack()
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operands.push(num)
            i -= 1   
        elif expression[i] == '(':
            operators.push(expression[i])
        elif expression[i] == ')':
            while operators.peek() != '(':
                apply_operator(operands, operators.pop())
            operators.pop()  # Remove '(' from the stack
        elif expression[i] in precedence:
            while (not operators.is_empty() and operators.peek() in precedence and
                   precedence[operators.peek()] >= precedence[expression[i]]):
                apply_operator(operands, operators.pop())
            operators.push(expression[i])
        i += 1

    while not operators.is_empty():
        apply_operator(operands, operators.pop())

    return operands.pop()


def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip() == '--------':  # Separator line
                outfile.write('----\n')
            else:
                result = evaluate_expression(line.strip())
                outfile.write(f"{result}\n")

input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)
