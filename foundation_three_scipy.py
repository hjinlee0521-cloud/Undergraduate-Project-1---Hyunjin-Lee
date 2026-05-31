import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sympy as smp

#Optimization
from scipy.optimize import minimize
#minimizing y = (x-3)^2
# def f(x):
#     return (x-3)**2

# res = minimize(f, 2)
# print(res)

#minimizing f(x, y) = (x-1)^2 + (y-2.5)^2
#constraints: x - 2y + 2 >= 0 , -x - 2y + 6 >= 0, -x + 2y + 2 >= 0, x >= 0, y >= 0
# f = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2
# cons = ({'type': 'ineq', 'fun': lambda x: x[0]-2*x[1]+2},
#         {'type': 'ineq', 'fun': lambda x: -x[0]-2*x[1]+6},
#         {'type': 'ineq', 'fun': lambda x: -x[0]+2*x[1]+2},
#         )
# bnds = ((0, None), (0, None))
# res = minimize(f, (2,0), bounds = bnds, constraints = cons)
# print(res)



#Interpolation
# x = np.linspace(0, 10, 10)
# y = x**2 * np.sin(x)
# plt.scatter(x, y)


from scipy.interpolate import interp1d
# f = interp1d(x, y, kind = 'cubic')
# x_dense = np.linspace(0, 10, 100)
# y_dense = f(x_dense)
# plt.plot(x_dense, y_dense)
# plt.show()



#Curve Fitting
# x_data = np.linspace(0, 10, 10)
# y_data = 3*x_data**2 + 2
# plt.scatter(x_data, y_data)
#fitting the curve to y = ax^2 + b
from scipy.optimize import curve_fit

# def func(x, a, b):
#     return a*x**2 + b

# popt, pcov = curve_fit(func, x_data, y_data, p0 = (1, 1))
# print(popt)



#Special Functions
from scipy.special import jv
#Leplace's Equation in Polar Coords
# x = np.linspace(0, 10, 100)
# plt.plot(x, jv(3,x))
# plt.show()


#Calculus
#Differentiation --> 이제 sympy 로 넘어가서 못씀ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# from scipy.misc import derivative
# def f(x):
#     return x**2 * np.sin(2*x) * np.exp(-x)
# x = np.linspace(0, 1, 100)
# plt.plot(x, f(x))
# plt.plot(x, derivative(f, x, dx=1e-6))
# plt.show()

#Integration
from scipy.integrate import quad
# integrand = lambda x: x**2 * np.sin(x) * np.exp(-x)
# integral, integral_error = quad(integrand, 0, 1)
# print(integral)
# print(integral_error)

#Double Integration
from scipy.integrate import dblquad
# integrand = lambda x, y: np.sin(x+y**2)
# lwr_y = lambda x: -x
# upr_y = lambda x: x**2
# integral, integral_error = dblquad(integrand, 0, 1, lwr_y, upr_y)
# print(integral)
# print(integral_error)


#n dimension Integration --> nqaud



#Differential Equations
from scipy.integrate import odeint
#v' - av^2 + B = 0, v(0) = 0
# def dvdt(v, t):
#     return 3*v**2 - 5 #setting a = 3, B=5
# v0 = 0
# t = np.linspace(0, 1, 100)
# sol = odeint(dvdt, v0, t)
# print(sol.T[0])


#Coupled First Order ODEs
# y1' = y1 + y2^2 + 3x, y1(0) = 0
# y2' = 3y1 + y2^3 - cos(x)

# def dSdx(S, x):
#     y1, y2 = S
#     return [y1+y2**2+3*x, 3*y1+y2**3-np.cos(x)]

# y1_0 = 0
# y2_0 = 0
# S_0 = (y1_0, y2_0)
# x = np.linspace(0, 1, 100)
# sol = odeint(dSdx, S_0, x)
# print(sol)

# y1 = sol.T[0]
# y2 = sol.T[1]

# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.show()



#Second Order ODEs
# x'' - sin(x) = 0
# S = (x, w)

# def dSdt(S, t):
#     x, w = S
#     return [w, np.sin(x)]

# x0 = np.pi/4
# w0 = 0 
# S0 = (x0, w0)

# t = np.linspace(0, 20, 100)
# sol = odeint(dSdt, S0, t)
# x, w = sol.T

# print(sol)
# plt.plot(t, x)
# plt.show()


#Linear Algebra
from scipy.linalg import solve_triangular

#ax = b
# a = np.array([[3, 0, 0, 0],
#               [2, 1, 0, 0],
#               [1, 0, 1, 0],
#               [1, 1, 1, 1]]) #lower triangular
# b = np.array([4, 2, 4, 2])
# x = solve_triangular(a, b, lower=True)
# print(x)


#Toeplitz Matrices (Matrices with constant diagonals)

from scipy.linalg import solve_toeplitz, toeplitz

#ax = b
# c = np.array([1, 3, 6, 10]) #first column of T
# r = np.array([1, -1, -2, -3]) #first row of T
# b = np.array([1, 2, 2, 5])
# x = solve_toeplitz((c,r),b)
# print(x)


#Eigenvalue Problems
from scipy.linalg import eigh_tridiagonal
# ax = lambda x 
# d = 3*np.ones(4)
# e = -1 * np.ones(3)
# w, v = eigh_tridiagonal(d, e)

# A = np.diag(d) + np.diag(e, k=1) + np.diag(e, k=-1)

# print(A@v.T[1])


#Statistics
from scipy.stats import beta
#Basic Statistics
a, b = 2.5, 3.1 
# mean, var, skew, kurt = beta.stats(a, b, moments = 'mvsk')
# print([mean, var, skew, kurt])

#Probability Distribution Plotting
# print(beta.ppf(0.01, a, b))

# x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99, a, b), 100)
# plt.plot(x, beta.ppf(x, a, b))
# plt.show()


#Multinomial Distribution
# from scipy.stats import multinomial 
# #Rolling a die
# p = np.ones(6)/6
# mul = multinomial.pmf([6, 0, 0, 0, 0, 0], n=6, p = p)
# print(mul)

# n = multinomial.rvs(n=100, p=p, size = 5)
# print(n)





#Sympy
#Basic Math
from sympy import symbols
x = smp.symbols('x')
# print(x)
# y = smp.sin(x)
# print(y)
# print(y-x)

y = x**2 + 4*x + 3
# print(y)
z = y**2
# print(z)
# print(z.factor())
# print(z.expand())


#symp.solve(f, x) finds the value x that makes f(x) = 0
# smp.solve(z, x)
# print(smp.solve(z, x))
# print(smp.solve(smp.sin(x), x))

# x = smp.symbols('x')
# print(smp.solve(x**2 + 1, x))

# x = smp.symbols('x', real = True)
# print(smp.solve(x**2 + 1, x))

# x = smp.symbols('x', real = True, positive = True)
# print(smp.solve(x**2 + 1, x))

x, y, z = smp.symbols('x y z')
# F = x**2 + smp.sin(z)*y
# # print(F)

# x_sols = smp.solve(F, x)
# # print(x_sols)

# y_sols = smp.solve(F, y)
# # print(y_sols)

# z_sols = smp.solve(F, z)
# # print(z_sols)


# expr = z_sols[0]
# print(expr)
# expr_f = smp.lambdify([x,y], expr) #making it into a workable function 
# print(expr_f(1, 2))

# x_num = np.linspace(0, 1, 100)
# y_num = 2
# plt.plot(x_num, expr_f(x_num, y_num))
# plt.show()


# #substitution
# F.subs([(y, 3), (z, smp.pi/2)])
# print(F.subs([(y, 3), (z, smp.pi/2)]))




#First year Calculus 
#Limits 
v = smp.limit(smp.sin(x/2 + smp.sin(x)), x, smp.pi)
# print(v)


#Derivatives
d = smp.diff(((1 + smp.sin(x))/(1 - smp.cos(x)))**2, x)
# print(d)


# f, g = smp.symbols('f g', cls = smp.Function)
# g = g(x)
# f = f(x+g)
# dfdx = smp.diff(f, x)
# print(dfdx)

# print(dfdx.subs([(g, smp.sin(x))]).doit()) #call 'doit'



#Integral
# ans = smp.integrate(smp.csc(x)*smp.cot(x), x)


# #Definite Integral
# ans1 = smp.integrate(smp.exp(x) / smp.sqrt(smp.exp(2*x) + 9), (x, 0, smp.log(4)))
# # print(ans1)

# t = smp.symbols('t')
# ans2 = smp.integrate(x**10 * smp.exp(x), (x, 1, t))
# print(ans2)




#Multivariable Calculus
x, y, z, u1, u2, u3, v1, v2, v3, t = smp.symbols('x y z u_1 u_2 u_3 v_1 v_2 v_3 t')
u = smp.Matrix([u1, u2, u3])
v = smp.Matrix([v1, v2, v3])

# print(v)

#Vector Calculation

#Vector Addition/Multiplication
# print(2*u + v)

#Dot product
# print(u.dot(v))

#Cross Product
# print(u.cross(v))


#Norm
# print(u.norm())

#projection of u on to v
proj_v_u = u.dot(v) / v.norm()**2 * v
print(proj_v_u)







