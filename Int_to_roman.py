def int_to_roman(num):
    if num > 3999 or num <= 0:
        return None
    conv = {
        1:'I',  10:'X',  100:'C',  1000:'M',
        5:'V',  50:'L',  500:'D',  5000:''
    }
    roman = ''
    x = 1
    while num > 0:
        dig = num % 10
        if dig % 5 == 4:
            a = conv[x]
            b = conv[(dig + 1) * x]
        else:
            a = conv[x * 5] * (dig // 5)
            b = conv[x] * (dig % 5)
        roman = a + b + roman
        num //= 10
        x *= 10
    return roman