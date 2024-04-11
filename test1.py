def sub_str_num(source_str, target_str):
    for char in target_str:        # target_str中存在字符，但source_str不存在
        if char not in source_str:
            return -1
    cnt = 0   #最少子序列数
    pos = 0   #标记下次循环开始位置
    for i in range(len(target_str)):
        for j in range(pos, len(source_str)):
            if j == len(source_str)-1:   #遍历完source_str, 找出一个最长子序列，cnt++。
                cnt += 1
                pos = 0
                break
            if target_str[i] == source_str[j]:  # 两个字符相同，从j的下一个位置开始遍历。
                pos = j + 1
                break
    return cnt

if __name__ == '__main__':
    # 测试数据
    source_str = 'abc'
    target_str = 'abcbc'
    print(sub_str_num(source_str,  target_str))