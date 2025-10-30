from stack import Stack 

class PostfixEvaluator:
    def evaluate(self, expression):
        stack = Stack()
       
        for token in expression.split(): #a token is an element in the expression
            try:
                number = int(token)
                stack.push(number) # add a number to the stack
                continue
            except ValueError:
                pass

            # Pop two numbers aka remove them from the stack...
            rhs = stack.pop()   # right
            lhs = stack.pop()   # left

            if token == "+":
                result = lhs + rhs
            elif token == "-":
                result = lhs - rhs
            elif token == "*":
                result = lhs * rhs
            elif token == "/":
                if rhs == 0:
                    raise Exception("division by zero")
                result = lhs // rhs  
            else:
                raise ValueError(f"Unknown operator: {token}")

            # Push the result back
            stack.push(result)

        # Test that one number is left in the stack
        if stack.size() != 1:
            raise ValueError("Invalid postfix expression.")
        return stack.pop()
