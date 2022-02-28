import math
import gmpy2

bg = gmpy2.get_context()

def function(x, y):
    return 1/(x+math.exp(y))

def Euler(x0, x1, y0, n):
    h = (x1-x0)/n
    xi = x0
    yi = y0
    for i in range(n):
        y_predict = yi + h*function(xi,yi)
        y_new = yi + h/2*(function(xi,yi)+function(xi+h,y_predict))
        xi += h
        yi = y_new
    return yi
        
def calculate_para(x0, x1, precision):
    xrange = x1 - x0
    upper_bound = 0.25 * 10**int(-precision)
    n = 1
    m = 1
    h = xrange / n
    while True:
        if (1+h+0.5*h*h)**(n+1) * (1.25*h*h) < upper_bound:
            break
        else:
            n += 1
            h = xrange / n
    while True:
        if (1+h+0.5*h*h)**(n+1) * (10**(-m)/(2*h)) < upper_bound:
            break
        else:
            m += 1
    return n, m

if __name__ == '__main__':
    x0, y0, x1, precision = 0, 0, 2, 6
    n, m = calculate_para(x0, x1, precision)
    # print(n)
    # print(m)
    bg.precision = int(math.ceil(10*(m-1)/3)+1)
    x0, x1, y0 = gmpy2.mpfr(x0), gmpy2.mpfr(x1), gmpy2.mpfr(y0)
    result = Euler(x0, x1, y0, n)
    print(result)
