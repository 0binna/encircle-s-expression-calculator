import sys


class SExpressionCalc:

    def calculator(self, str_input):
        while True:
            if "(" not in str_input:
                return int(str_input)

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
                return result
            else:
                str_input = str_input[:idx_left_brace] + \
                    str(result) + str_input[idx_right_brace+1:]

    def calc_add(self, expr):
        result = int(expr[1]) + int(expr[2])
        return result

    def calc_multiply(self, expr):
        result = int(expr[1]) * int(expr[2])
        return result


def main():
    print(SExpressionCalc().calculator(sys.argv[1]))


if __name__ == '__main__':
    main()
