import triangle
import circle
import square

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']

sizes = {
    "area-circle": 1,
    "perimeter-circle": 1,
    "area-square": 1,
    "perimeter-square": 1,
    "area-triangle": 3,
    "perimeter-triangle": 3
}


def calc(fig, func, size):
    assert fig in figs, "Unsupported figure"
    assert func in funcs, "Unsupported function"

    if fig == "circle":
        if func == "area":
            return circle.area(*size)
        elif func == "perimeter":
            return circle.perimeter(*size)
    elif fig == "square":
        if func == "area":
            return square.area(*size)
        elif func == "perimeter":
            return square.perimeter(*size)
    elif fig == "triangle":
        if func == "area":
            return triangle.area(*size)
        elif func == "perimeter":
            return triangle.perimeter(*size)


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(
            f"Enter figure name, available are {figs}:\n"
        )

    while func not in funcs:
        func = input(
            f"Enter function name, available are {funcs}:\n"
        )

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        try:
            size = list(map(float, input(
                f"Input figure sizes separated by space 
				(expected {sizes.get(f'{func}-{fig}', 1)} values):\n"
            ).split()))
            if any(s <= 0 for s in size):
                print("All sizes must be positive")
                size = []
        except ValueError:
            print("Please enter valid numbers")

    result = calc(fig, func, size)
    print(f"The result is: {result}")
