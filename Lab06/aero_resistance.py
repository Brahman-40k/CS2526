from math import pi


def main():
    wire_gauge = int(input("Enter the wire_gauge: "))
    length = float(input("Enter the length of wire: "))
    result = copper_wire_resistance(length, wire_gauge)
    print(f"The resistance of copper is {result} Ω")


def diameter(wire_gauge):
    return 0.127 * 92 ** ((36 - wire_gauge) / 39)


def copper_wire_resistance(length, wire_gauge):
    D = diameter(wire_gauge)
    D /= 1000
    ro = 1.678 * 10 ** (-8)
    resistance = (ro * length * 4) / (pi * D**2)
    return resistance


if __name__ == "__main__":
    main()
