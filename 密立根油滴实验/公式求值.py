
import math

# 输入参数
eta = 0.0000183  # 空气粘度
l = 0.0016  # 匀速下降的距离
rho = 979  # 油滴密度
g = 9.794  # 重力加速度
b = 0.00822  # 修正常数
P = 10133  # 大气压强
d = 0.005  # 电场宽度
e_0 = 0.00000000000000000016021773  # 真空介电常数

# 计算油滴半径
def cul_a(eta,l,rho,g,t_avg):
    return (9*eta*l/(2*rho*g*t_avg))**0.5

# 计算电荷量
def cul_q(U_avg,a,t_avg,rho,g,d,eta,b,P):
    return (18*math.pi*d/(U_avg*(2*rho*g)**0.5))*(eta*l/((1 + b/(P*a))*t_avg))**1.5

# 计算元电荷数
def cul_n(q, e_0):
    return q/e_0, round(q/e_0)

# 计算单位电荷
def cul_e1(q, n_int):
    return q/n_int

# 计算相对误差
def cul_E(e_0, e_1):
    return abs(e_0 - e_1)/e_0*100


if __name__ == '__main__':
    t_avg = 29.58
    U_avg = 155
    a = cul_a(eta, l, rho, g, t_avg)
    q = cul_q(U_avg, a, t_avg, rho, g, d, eta, b, P)
    n, n_int = cul_n(q, e_0)
    e1 = cul_e1(q, n_int)
    E = cul_E(e_0, e1)
    print(a)
    print(q)
    print(n)
    print(n_int)
    print(e1)
    print(E)