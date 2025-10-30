
from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter

def run_postfix_tests():
   
    postfix_cases = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -",
    ]

    pe = PostfixEvaluator()
    print("----- Postfix Evaluator -----")
    for expr in postfix_cases:
        result = pe.evaluate(expr)
        print(f"[{expr}] = {result}")

def run_infix_tests():
    infix_cases = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A * B + C / D",
        "( A + B ) * ( C - D )",
        "A + B * C - D / E",
        "A * ( B + C ) / D",
        "( A + B * C ) / ( D - E )",
        "A +  ( B - C ) * D",
        "( A + B * ( C - D ) ) / E",
    ]

    conv = InfixToPostfixConverter()
    print("\n----- Infix to Postfix Converter -----")
    for expr in infix_cases:
        postfix = conv.convert(expr)
        print(f"[{expr}] -> [{postfix}]")

if __name__ == "__main__":
    run_postfix_tests()
    run_infix_tests()

