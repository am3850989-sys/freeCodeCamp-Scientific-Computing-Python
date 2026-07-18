def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_line = []
    bottom_line = []
    dashes = []
    answers = []
    
    for problem in problems:
        num1, operator, num2 = problem.split()
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
            
        width = max(len(num1), len(num2)) + 2
        top_line.append(num1.rjust(width))
        bottom_line.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)
        if show_answers:
            ans = str(eval(problem))
            answers.append(ans.rjust(width))
            
    arranged = '    '.join(top_line) + '\n' + '    '.join(bottom_line) + '\n' + '    '.join(dashes)
    if show_answers:
        arranged += '\n' + '    '.join(answers)
        
    return arranged
