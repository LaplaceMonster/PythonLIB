from scipy.optimize import fsolve
import math
from tkinter import filedialog
import numpy as np
def bruggeman(eps_water, eps_oil, vol_frac_water, eps_guess=10):
    """
    使用 Bruggeman 模型计算水-油混合物的等效介电常数。
    
    参数：
    eps_water : 水的介电常数（高介电）
    eps_oil   : 油的介电常数（低介电）
    vol_frac_water : 水的体积分数（0 到 1 之间）
    eps_guess : 初始猜测值，默认为 10
    
    返回：
    等效介电常数（float）
    """
    if not 0 <= vol_frac_water <= 1:
        raise ValueError("水的体积分数必须在 0 到 1 之间。")

    equation = lambda eps_eff: (
        vol_frac_water * (eps_water - eps_eff) / (eps_water + 2 * eps_eff) +
        (1 - vol_frac_water) * (eps_oil - eps_eff) / (eps_oil + 2 * eps_eff)
    )

    eps_eff_solution = fsolve(equation, eps_guess)
    return eps_eff_solution[0]

def S21_MAG(Dielectric_constant,Loss_tangent,length,Fre=2.45e9):
    '''
    计算传播损耗/动态范围 使用S21来表征 S21=10*lg(Pout/Pin)  此列中默认Pin为1mW(0dBm)
    Dielectric_constant:介电常数
    Loss_tangent:介电损耗正切
    length:微波的传播距离
    Fre=2.45e9:频率默认为2.45GHz
    '''
    lambda1=3e8/Fre  #波长=光速/频率
    #损耗系数计算
    Pin=1
    alpha=(math.pi/lambda1)*math.sqrt(Dielectric_constant/2*(math.sqrt(1+Loss_tangent**2)-1))
    Pout=Pin*math.exp(-2*alpha*length) #输出功率
    return 10*math.log10(Pout/Pin)*2 #S21计算
def S21_PHS(Dielectric_constant,length,Fre=2.45e9):
    '''
    计算透射待测物质后相位差（相对于真空下）
    即S21的相位信息。
    '''
    lambda_cur=3e8/Fre
    return 360*length/lambda_cur*math.sqrt(Dielectric_constant)

def DebyeModel(Eps,EpsH,Relationtime,Fre=2.45e9):
    W=math.pi*Fre*2
    Relationtime *= 1e-12 
    Re=EpsH+((Eps-EpsH)/(1+W**2*Relationtime**2))
    Im=(Eps-EpsH)*W*Relationtime/(1+W**2*Relationtime**2)
    Loss_tangent=Im/Re
    return Re,Im,Loss_tangent


oil_dielectric_constant = 2.5  # 油的介电常数
oil_loss_tangent = 0.002  # 油的损耗正切

t = np.arange(0, 31, 1)  # 温度0——60度

Dielectric_constant_t = t*t*-0.001532 - 0.1839*t + 82.72
loss_t = t*t*0.00005715 - 0.006453*t + 0.2451

Water_content = np.arange(0, 1.1, 0.1)  # 水的体积分数

for j in t:#温度的循环
    for i in Water_content:#h水的体积分数循环
    
        eps_water = Dielectric_constant_t[j]# 水的介电常数
        eps_oil = oil_dielectric_constant# 油的介电常数
        vol_frac_water = i# 水的体积分数
        eps_guess = 10# 介电常数初始猜测值
        eps_eff = bruggeman(eps_water, eps_oil, vol_frac_water, eps_guess)
        
        loss_water = loss_t[j]
        loss_oil = oil_loss_tangent
        loss_guess = 0.01  # 损耗正切初始猜测值
        loss_tangent = bruggeman(loss_water, loss_oil, vol_frac_water,loss_guess )
        
        # 计算 S21 的相位和幅度
        length = 0.05  # 假设传播距离为 0.1 米
        s21_phase = S21_PHS(eps_eff, length)
        s21_magnitude = S21_MAG(eps_eff, loss_tangent, length)
        
        print(f" 温度: {j}°C,水的体积分数: {i:.1f}, 等效介电常数: {eps_eff:.2f}, "
              f"损耗正切: {loss_tangent:.4f}, S21 相位: {s21_phase:.2f}°, "
              f"S21 幅度: {s21_magnitude:.2f} dB")


