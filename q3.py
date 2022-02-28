import math
import gmpy2

bg = gmpy2.get_context()

w_a = 0.56714329

def interval(t):
    n = 1
    b = math.sqrt(w_a)
    upper_bound = 0.25 * 10**int(-t)
    para = b * (24 + 156*w_a + 112*w_a*w_a + 16*w_a**3) * math.exp(w_a) / 2880
    while True:
        if para * (w_a/n/n)**2 < upper_bound:
            break
        else:
            n = n + 1
    return n, b/n

# def get_m(t):
#     m = 1
#     b = math.sqrt(w_a)
#     upper_bound = 0.25 * 10**int(-t)
#     para = 1.0/2/b + b/2*(1+w_a)*math.exp(w_a)
#     while True:
#         if para * 10**(-m) < upper_bound:
#             break
#         else:
#             m = m + 1
#     return m

def function(x):
    return x * x * math.exp(x*x)

def simpson(n, h):
    result = 0
    b = math.sqrt(w_a)
    for i in range(1, n):
        result += 2*function(i*h)
    for i in range(0, n):
        result += 4*function(i*h+h/2)
    result += function(b)
    result = h/6*result
    return b - result

if __name__ == '__main__':
    precision = 6
    n, h = interval(precision)
    # print(n)
    # print(h)
    # m = get_m(precision)
    # print(m)
    result = simpson(n, h)
    print(result)
    