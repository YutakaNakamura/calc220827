import sympy as sy

# original simplify atan
def simplify_atan(sympy, expr_y, expr_x):
    fx = sympy.simplify(expr_x)
    fy = sympy.simplify(expr_y)
    tan = fy / fx
    atan = sympy.atan(tan)
    theta = sympy.simplify(atan)
    return sympy.factor(theta)

# original simplify atan
def simplify_collect(sympy, expr_input, collect_expr):
    expr = expr_input
    # expr = sympy.factor(expr)
    expr = sympy.simplify(expr)
    # expr = sympy.factor(expr)
    expr = sympy.collect(expr, collect_expr)
    return expr

#Jupyter Notebookを使う場合
# sy.init_printing()

#motor params
Li = sy.Symbol("Li", real=True)
Lm = sy.Symbol("Lm", real=True)
A = sy.Symbol("A", real=True)
K = sy.Symbol("K", real=True)
theta_gamma = sy.Symbol("theta_gamma", real=True)
theta_re = sy.Symbol("theta_re", real=True)
theta_e = sy.Symbol("theta_e", real=True)

#gain
g_pi = sy.Symbol("g_pi", real=True)
g_pm = sy.Symbol("g_pm", real=True)
g_ni = sy.Symbol("g_ni", real=True)
g_nm = sy.Symbol("g_nm", real=True)
g_pi = A*(1+K)*Li
g_pm = A*(-(1-K)*Lm)
g_ni = A*(1-K)*Li
g_nm = A*(-(1+K)*Lm)

#complex amp
c_p = sy.Symbol("c_p", real=True)
s_p = sy.Symbol("s_p", real=True)
c_n = sy.Symbol("c_n", real=True)
s_n = sy.Symbol("s_n", real=True)
c_p = g_pi + g_pm * sy.cos(2*theta_gamma)
s_p =        g_pm * sy.sin(2*theta_gamma)
c_n = g_ni + g_nm * sy.cos(2*theta_gamma)
s_n =        g_nm * sy.sin(2*theta_gamma)

#variable num
C_2p = sy.Symbol("C_2p", real=True)
S_2p = sy.Symbol("S_2p", real=True)
C_2p = c_p*c_n - s_p*s_n
S_2p = s_p*c_n + c_p*s_n
theta_re = sy.atan(C_2p / S_2p)

#hosooka
#complex amp
c_pt = sy.Symbol("c_pt", real=True)
s_pt = sy.Symbol("s_pt", real=True)
c_nt = sy.Symbol("c_nt", real=True)
s_nt = sy.Symbol("s_nt", real=True)
c_pt = c_p * sy.cos(theta_e) - s_p * sy.sin(theta_e)
s_pt = s_p * sy.cos(theta_e) + c_p * sy.sin(theta_e)
c_nt = c_n * sy.cos(theta_e) - s_n * (-sy.sin(theta_e))
s_nt = s_n * sy.cos(theta_e) + c_n * (-sy.sin(theta_e))

print("--- hosooka's thesis ---")

print("eq.13")
print( (c_pt + c_nt).subs(K, 0) )
print( (s_pt - s_nt).subs(K, 0) )

print("eq.12 atan2")
y = (s_pt - s_nt).subs(K, 0)
x = (c_pt + c_nt).subs(K, 0)
print(simplify_atan(sy, y, x))

print("eq.15")
print( (c_pt).subs(K, 1) )
print( (s_pt).subs(K, 1) )
print("eq.14 atan2")
y = (s_pt).subs(K, 1)
x = (c_pt).subs(K, 1)
print(simplify_atan(sy, y, x))

print("--- original research(1) ---")
print("c,s delta, K=0")
print( (-c_pt + c_nt).subs(K, 0) )
print( (s_pt + s_nt).subs(K, 0) )
print("calculate atan")
y = (-c_pt + c_nt).subs(K, 0)
x = (s_pt + s_nt).subs(K, 0)
print(simplify_atan(sy, y, x))

print("c,s gamma, not 0 (eq.13 not 0)")
print( sy.factor((c_pt + c_nt)) )
print( sy.factor((s_pt - s_nt)) )
print("c,s delta, not 0")
print( sy.factor((-c_pt + c_nt)) )
print( sy.factor((s_pt + s_nt)) )

print("--- original research(2) ---")

print("p n expr")
print("@c_p tilde")
print( simplify_collect(sy,c_pt,sy.cos(theta_e)) )
print("@s_p tilde")
print( simplify_collect(sy,s_pt,sy.sin(theta_e)) )
print("@c_n tilde")
print( simplify_collect(sy,c_nt,sy.cos(theta_e)) )
print("@s_n tilde")
print( simplify_collect(sy,s_nt,sy.sin(theta_e)) )

#original 
#gamma delta tilde complex amp
c_gammat = sy.Symbol("c_gammat", real=True)
s_gammat = sy.Symbol("s_gammat", real=True)
c_deltat = sy.Symbol("c_deltat", real=True)
s_deltat = sy.Symbol("s_deltat", real=True)
c_gammat = c_pt + c_nt
s_gammat = s_pt - s_nt
c_deltat = -c_pt + c_nt
s_deltat = -(-s_pt - s_nt)

# print("gamma delta expr")
# print("@c_gamma tilde")
# print( simplify_collect(sy,c_gammat,sy.cos(theta_e)) )
# print("@s_gamma tilde")
# print( simplify_collect(sy,s_gammat,sy.sin(theta_e)) )
# print("@c_delta tilde")
# print( simplify_collect(sy,c_deltat,sy.cos(theta_e)) )
# print("@s_delta tilde")
# print( simplify_collect(sy,s_deltat,sy.sin(theta_e)) )

# print("gamma K=0")
# y = s_gammat.subs(K, 0)
# x = c_gammat.subs(K, 0)
# print(simplify_atan(sy, y, x))

# print("delta K=0")
# y = s_deltat.subs(K, 0)
# x = c_deltat.subs(K, 0)
# print(simplify_atan(sy, y, x))

# print("gamma delta atan")
# y = sy.factor(c_gammat)
# x = sy.factor(s_gammat)
# print(simplify_atan(sy, y, x))

# # 検算する
# print("calculate 220827-1")
# y = K*s_deltat - s_gammat
# x = -K*c_deltat + c_gammat
# print(sy.simplify(x))
# print(sy.simplify(y))
# print("calculate atan t")
# print(simplify_atan(sy, y, x))

print("@calculate 220827-2 my expr")
y = -(K*s_gammat + s_deltat)
x = K*c_deltat + c_gammat
print(simplify_collect(sy,x,sy.cos(theta_e)))
print(simplify_collect(sy,y,sy.sin(theta_e)))
print("@calculate atan my expr")
print(simplify_atan(sy, y, x))

# print("calculate 220827-2 my expr zikkenn")
# ta = -K*c_deltat + c_gammat
# tb =  K*s_gammat + s_deltat

# ta = simplify_collect(sy,ta,sy.cos(theta_e))
# tb = simplify_collect(sy,tb,sy.sin(theta_e))
# print(sy.simplify(ta))
# print(sy.simplify(tb))