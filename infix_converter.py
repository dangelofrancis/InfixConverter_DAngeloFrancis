
from stack import Stack

class InfixToPostfixConverter:
    def _is_number(self, token):
        try:
            int(token)
            return True
        except ValueError:
            return False

    def _is_variable(self, token):
        if token in ["+", "-", "*", "/", "(", ")"]:
            return False
        return any(ch.isalpha() for ch in token)

    def _is_operand(self, token):
        return self._is_number(token) or self._is_variable(token)

    def _precedence(self, operator):
        if operator in ("*", "/"):
            return 2
        if operator in ("+", "-"):
            return 1
        return 0  # not an operator

    def convert(self, expression):
        tokens = expression.split()

        output = []     # where we build the postfix
        ops = Stack()   # operator stack

        for token in tokens:
            if self._is_operand(token):
                # operands go straight to output
                output.append(token)

            elif token == "(":
                # add '(' so you know where to stop later
                ops.push(token)

            elif token == ")":
                # remove operators until matching '('
                while not ops.is_empty() and ops.peek() != "(":
                    output.append(ops.pop())
                if ops.is_empty():
                    raise ValueError("Mismatched parentheses: missing '('")
                ops.pop()  # discard the '('

            else:
                # while top of stack has operator with >= precedence, pop it
                while (not ops.is_empty() 
                       and ops.peek() != "("
                       and self._precedence(ops.peek()) >= self._precedence(token)):
                    output.append(ops.pop())
                ops.push(token)

        # pop leftover operators
        while not ops.is_empty():
            top = ops.pop()
            if top in ("(", ")"):
                raise ValueError("Mismatched parentheses")
            output.append(top)

        # join with spaces 
        return " ".join(output)
