from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
from sympy import symbols, sin
from galgebra.printer import Format, xpdf
from galgebra.ga import Ga

Format()
coords = (x, y, z) = symbols('x y z', real=True)
(o3d, ex, ey, ez) = Ga.build('e*x|y|z', g=[1, 1, 1], coords=coords)
X = x * ex + y * ey + z * ez
I = o3d.i
v = o3d.mv('v', 'vector')
f = o3d.mv('f', 'scalar', f=True)
A = o3d.mv('A', 'vector', f=True)
dd = v | o3d.grad
lap = o3d.grad * o3d.grad
print(r'\bm{X} =', X)
print(r'\bm{v} =', v)
print(r'\bm{A} =', A)
print(r'%\bm{v}\cdot\nabla =', dd)
print(r'%\nabla^{2} =', lap)
print(r'%\bm{v}\cdot\nabla f =', dd * f)
print(r'%\nabla^{2} f =', lap * f)
print(r'%\nabla^{2} \bm{A} =', lap * A)
print(r'%\bar{\nabla}\cdot v =', o3d.rgrad | v)
Xgrad = X | o3d.grad
rgradX = o3d.rgrad | X
print(r'%\bm{X}\cdot \nabla =', Xgrad)
# FIXME This outputs incorrectly, the scalar part 3 is missing
print(r'%\bar{\nabla}\cdot \bm{X} =', rgradX)
# FIXME The following code complains: 
# ValueError: In Dop.Add complement flags have different values: False vs. True
# com = Xgrad - rgradX
# print(r'%\bm{X}\cdot \nabla - \bar{\nabla}\cdot \bm{X} =', com)
sph_coords = (r, th, phi) = symbols('r theta phi', real=True)
(sp3d, er, eth, ephi) = Ga.build('e', g=[1, r**2, r**2 * sin(th)**2],
                                 coords=sph_coords, norm=True)
f = sp3d.mv('f', 'scalar', f=True)
lap = sp3d.grad * sp3d.grad
print(r'%\nabla^{2} = \nabla\cdot\nabla =', lap)
print(r'%\lp\nabla^{2}\rp f =', lap * f)
print(r'%\nabla\cdot\lp\nabla f\rp =', sp3d.grad | (sp3d.grad * f))
# FIXME crop didn't work, but pdf can be generated with TexLive 2017 installed
xpdf(paper='landscape', crop=True)
