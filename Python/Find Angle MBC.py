import math 
degree_sign = u"\N{DEGREE SIGN}"
AB = int(input())
BC = int(input())
hypotenuse =  math.sqrt(AB**2 + BC**2)
MBC = math.acos((BC*0.5)/(hypotenuse*0.5))

print(f'{round(math.degrees(MBC))}{degree_sign}')