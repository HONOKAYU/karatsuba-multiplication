# 计算数字的幂次补零
def get_order(n_str):
    n_bits = len(n_str)
    i = 1
    order = 0
    while i < n_bits:
        order += 1
        i *= 2
    return order


# 预补零
def prepend_zero(n_str, length):
    return '0' * length + n_str


# 后补零
def append_zero(n_str, length):
    return n_str + '0' * length


def karatsuba(n1, n2):
    # 转化位字符串处理问题
    n1_str, n2_str = str(n1), str(n2)

    # 处理正负号问题
    if n1_str[0] == '-':
        return -karatsuba(-n1, n2)
    if n2_str[0] == '-':
        return -karatsuba(n1, -n2)

    # 终止条件
    if n1 < 10 or n2 < 10:
        return n1 * n2

    # 两个数字预补零
    n1_str_len, n2_str_len = len(n1_str), len(n2_str)
    order = get_order(n1_str) if n1_str_len < n2_str_len else get_order(n2_str)

    n1_app_len = 2 ** order - n1_str_len
    n2_app_len = 2 ** order - n2_str_len

    app_n1_str = prepend_zero(n1_str, n1_app_len)
    app_n2_str = prepend_zero(n2_str, n2_app_len)

    # 将数字拆分
    split_pos = (2 ** order) // 2
    a, b = int(app_n1_str[:split_pos]), int(app_n1_str[split_pos:])
    c, d = int(app_n2_str[:split_pos]), int(app_n2_str[split_pos:])

    m0 = karatsuba(a, c)
    m1 = karatsuba(b, d)

    ab = a + b
    cd = c + d
    m2 = karatsuba(ab, cd) - m0 - m1

    # m0,m2后补零
    m0_str, m2_str = str(m0), str(m2)
    app_m0_str = append_zero(m0_str, 2 * split_pos)
    app_m2_str = append_zero(m2_str, split_pos)

    return int(app_m0_str) + int(app_m2_str) + m1


if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    print(karatsuba(x, y))
