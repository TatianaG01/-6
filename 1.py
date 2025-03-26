from fileinput import filename


def parse_equation(coef) :
    n = len(coef)
    if n == 2:
        return Equation(coef[0] , coef[1])
    elif n == 3:
        return QuadraticEquation (coef[0],coef[1],coef[2])
    elif == 5:
        return BiQuadraticEquation (coef[0],coef[2],coef[4])
    else:
        return None

    def read-file(filename):
    equation = []
    with open (filename, 'r') as f:
        for line in f:
            coef = list(map(float,line,split()))
            equation = parse_equation(coef)
            if equation:
                equations.append(equation)
                return equations
