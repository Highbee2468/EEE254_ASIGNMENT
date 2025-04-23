def f(p):
    return -0.5 * p**2 + 80 * p - 500
def df(p):
    return -1 * p + 80

result = compare_bisection_newton(f, df, a=0, b=200, x0=50)
print("Break-even Point Finder:")

for method, outcome in result.items():
    print(f"{method}:")
    if "error" in outcome:
        print(f"  Error: {outcome['error']}")
    else:
        print(f"  Break-even price: {outcome['root']:.4f}")
        print(f"  Steps taken: {outcome['steps']}")
