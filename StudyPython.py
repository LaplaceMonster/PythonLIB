from scipy.optimize import fsolve
import math
from tkinter import filedialog
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
    return 10*math.log10(Pout/Pin) #S21计算
def S21_PHA(Dielectric_constant,length,Fre=2.45e9):
    '''
    计算透射待测物质后相位差（相对于真空下）
    即S21的相位信息。
    '''
    lambda_cur=3e8/Fre
    return 360*length/lambda_cur*math.sqrt(Dielectric_constant)

eps_water = 82 # 水的介电常数
eps_oil = 2.5    # 油的介电常数

loss_water = 0.25 # 水的损耗正切
loss_oil = 0.0008  # 油的损耗正切

S21_water = S21_MAG(eps_water, loss_water, 0.05)*2  # 水的 S21
S21_oil = S21_MAG(eps_oil, loss_oil, 0.05)*2  # 油的 S21

print(f"水的 S21: {S21_water:.2f} dB")
print(f"油的 S21: {S21_oil:.4f} dB")

S21_PHA_water = S21_PHA(eps_water, 0.05)  # 水的相位差
S21_PHA_oil = S21_PHA(2.5, 0.05)  # 油的相位差

print(f"水的相位差: {S21_PHA_water:.2f} °")
print(f"油的相位差: {S21_PHA_oil:.2f} °")