import math

def triangle(radius):
    sq = (math.pi)*((radius)**2)
    lenth = 2*((math.pi)*(radius))
    print(sq, lenth)

def main():
    radius = int(input("Введите радиус:"))
    triangle(radius)

if __name__ == main():
    main()