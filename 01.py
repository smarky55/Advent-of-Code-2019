import math


def fuel(mass):
    return math.floor(int(mass)/3) - 2

def fuel2(mass):
    m_fuel = fuel(mass)
    if m_fuel > 8:
        return m_fuel + fuel2(m_fuel)
    else:
        return m_fuel


with open('input/01.txt') as inFile:
    modules = inFile.readlines()
    print(sum(map(fuel, modules))) # Part 1

    print(fuel2(1969))
    # Part 2
    print(sum(map(fuel2, modules)))