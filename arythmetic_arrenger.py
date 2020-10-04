def arythmetic_arrenger(list):
    if len(list) > 5:
        e1 = "Error: Too many problems."
        return e1
    elif 1 <= len(list) < 5:
        lines = []
        for problem in list:
            subs = problem.split()
            a = subs[0]
            operator = subs[1]
            b = subs[2]

            if len(a) > len(b):
                max_length = len(a)
            else:
                max_length = len(b)

            if (a.isdigit() and b.isdigit()):
                a_int = int(a)
                b_int = int(b)
            else:
                e2 = "Error: Too many problems."
                return e2

            if operator == '+':
                c_int = a_int + b_int
            elif operator == '-':
                c_int = a_int - b_int
            else:
                return "Error: Operator must be '+' or '-'."

            first_line = a.rjust(max_length + 2)
            second_line = operator + b.rjust(max_length + 1)
            third_line = "--" + (max_length * "-")

            c = str(c_int)
            fourth_line = c.rjust(max_length + 2)

            object = [first_line, second_line, third_line, fourth_line]
            lines.append(object)

        result = [print(*line, sep='    ')for line in zip(*lines)]
        return result


if __name__ == '__main__':
    arythmetic_arrenger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
