import sympy as sp

#Defintion des symbols (Variables)
m1, m2, o1, o2 = sp.symbols('m1, m2, o1, o2')

#Lecture des constantes
mr  = float(input("Donner Mr : "))
d  = float(input("Donner D : "))
ro  = float(input("Donner Ro : "))
f  = float(input("Donner F :"))
r  = float(input("Donner R : "))
l  = float(input("Donner L : "))
e = float(input("Donner E : "))

#Definition des equations
eq1 = sp.Function('eq1')
eq1 = sp.Function('eq2')
eq3 = sp.Function('eq3')
eq4 = sp.Function('eq4')

eq1 = sp.Eq(mr*d + m1*ro*sp.cos(o1) + m2 * ro * sp.cos(o2), 0)
eq2 = sp.Eq(m1 * ro * sp.sin(o1) + m2 * ro * sp.sin(o2), 0)
eq3 = sp.Eq(e + l/2 * ro *(m1 * sp.sin(o1) - m2 * sp.sin(o2)), 0)
eq4 = sp.Eq(f + l/2 * ro *(m1 * sp.cos(o1) - m2 * sp.cos(o2)), 0)

#Affichage des equations
print(eq1)
print(eq2)
print(eq3)
print(eq4)

#Affichage des resultats
sol = sp.solve([eq1, eq2, eq3, eq4], [m1, m2, o1, o2], dict=True)
print(sol)

for v in sol:
    print(v)

