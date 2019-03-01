from galgebra.printer import  Format, xpdf, Fmt
Format()
from sympy import symbols, Rational, latex
from galgebra.ga import Ga

# st4: Spacetime Algebra I
st4coords = (t,x,y,z) = symbols('t x y z', real=True) 
st4 = Ga('e_t e_x e_y e_z', g=[1,-1,-1,-1], coords=st4coords)
#(et, ex, ey, ez) = st4.mv()
(e_t,e_x,e_y,e_z) = st4.mv()
(e__t,e__x,e__y,e__z) = st4.mvr(norm = False) 

Format(Fmode = True, Dmode = True)

(grad,rgrad) = st4.grads()

import sys
half = Rational(1,2)

print(r'\mbox{Python version = }', sys.version)

s = st4.mv('s','scalar',f = True)
a = st4.mv('a','vector',f = True)
b = st4.mv('b','vector',f = True)
B = st4.mv('B','bivector',f = True)
C = st4.mv('C',3)
I = st4.mv('I','pseudo')
S = st4.mv('S','spinor',f = True)
M = st4.mv('M','mv',f = True)

print(r'\bm{a} = ', a)

print(M.Fmt(2,r'\bm{M}'))

print((a*a).Fmt(1,r'\bm{a} \bm{a}'))

print(a.inv().Fmt(3,r'\bm{a}^{-1}'))

print((M.grade(1) * M.grade(1)).\
 Fmt(1,r'\langle \bm{M} \rangle _1 \langle \bm{M} \rangle _1'))

M1inv = M.grade(1).inv()
print(M1inv.Fmt(3,r'\langle \bm{M} \rangle _1 ^{-1}'))

print(M.grade(3).Fmt(2,r'\langle \bm{M} \rangle _3'))

print((M.grade(3) * M.grade(3)).\
 Fmt(1,r'\langle \bm{M} \rangle _3 \langle \bm{M} \rangle _3'))

M3inv = M.grade(3).inv()
print(M3inv.Fmt(3,r'\langle \bm{M} \rangle _3^{-1}'))

xpdf(paper=(8,9))
