import sys


class SExpressionCalc:

    def calculator(self, str_input):
        if "(" not in str_input:
            return print(int(str_input))

        # Validate input
        validate = self.check_validation(str_input)

        while validate:
            # Extract innermost expression
            idx_right_brace = str_input.index(')')
            idx_left_brace = str_input[:idx_right_brace].rindex('(')
            expr = str_input[idx_left_brace + 1:idx_right_brace]
            expr = expr.split()

            function_call = expr[0]

            if function_call == "add":
                result = self.calc_add(expr)

            if function_call == "multiply":
                result = self.calc_multiply(expr)

            # Check if final expression is evaluated
            if idx_left_brace == 0:
                return print(result)
            else:
                str_input = str_input[:idx_left_brace] + \
                    str(result) + str_input[idx_right_brace+1:]

    def calc_add(self, expr):
        result = int(expr[1]) + int(expr[2])
        return result

    def calc_multiply(self, expr):
        result = int(expr[1]) * int(expr[2])
        return result

    def check_validation(self, str_input):
        parsed_string = ''
        for char in str_input:
            if char == '(':
                parsed_string += char + ' '
            elif char == ')':
                parsed_string += ' ' + char
            else:
                parsed_string += char

        expr_list = parsed_string.split()

        if expr_list[0] != '(' or expr_list[-1] != ')':
            print("Parenthesis missing")
            return False
        if expr_list[1] not in ['add', 'multiply']:
            print("No function call provided")
            return False
        if len(expr_list) < 5:
            print("Invalid syntax")
            return False
        return True


def main():
    if len(sys.argv) < 2:
        print('No input provided')
        return

    SExpressionCalc().calculator(sys.argv[1])


if __name__ == '__main__':
    main()
