def check_brackets(input_str):
    stack = []         # 栈，用来存储左括号索引
    output_str = ''    # 最后输出字符串
    output = [' ' for _ in range(len(input_str))]    #数组，存储输出
    for i in range(len(input_str)):
        if input_str[i] == '(':    #左括号入栈
            stack.append(i)
        elif input_str[i] == ')':  #遇到右括号，弹出一个左括号，或者标记"?"
            if stack:
                stack.pop()
            else:
                output[i] = '?'
        else:
            continue
    while stack:          #栈不空，说明左括号有多余，标记”X“
        i = stack.pop()
        output[i] = 'X'
    for char in output:
        output_str += char

    return input_str + "\n" + output_str


if __name__ == '__main__':
    # 测试数据
    test_cases = ["bge)))))))))",
                  "((IIII))))))",
                  "()()()()(uuu",
                  "))))UUUU((()"]
    for test_case in test_cases:
        print(check_brackets(test_case))
