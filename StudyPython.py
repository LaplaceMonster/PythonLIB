import math
import numpy
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def DebyeModel(Eps,EpsH,Relationtime,Fre=2.45):
    Fre=Fre*1e9  
    W=math.pi*Fre*2
    Relationtime *= 1e-12 
    Re=EpsH+((Eps-EpsH)/(1+W**2*Relationtime**2))
    Im=(Eps-EpsH)*W*Relationtime/(1+W**2*Relationtime**2)
    Loss_tangent=Im/Re
    return Re,Im,Loss_tangent

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
def S21_PHS(Dielectric_constant,length,Fre=2.45e9):
    '''
    计算透射待测物质后相位差（相对于真空下）
    即S21的相位信息。
    '''
    lambda_cur=3e8/Fre
    return 360*length/lambda_cur*(math.sqrt(Dielectric_constant)-1)


'''
温度	介电常数(静态)	高频极限介电常数	弛豫时间(ps)
-4.1	89.25	5.9	21.1
0	87.91	5.7	17.67
5	85.83	5.7	14.91
10	83.92	5.5	12.68
15	82.05	6	10.83
20	80.21	5.6	9.36
25	78.36	5.2	8.27
30	76.56	5.2	7.28
35	74.87	5.1	6.5
40	73.18	3.9	5.82
50	69.89	4	4.75
60	66.7	4.2	4.01

'''


Eps_list = {
    0:[87.91,5.7,17.67],
    10:[83.92,5.5,12.68],
    20:[80.21,5.6,9.36],
    30:[76.56,5.2,7.28],
    40:[73.18,3.9,5.82],
    50:[69.89,4,4.75],
    60:[66.7,4.2,4.01],
}

color_list = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']
fres = numpy.arange(1, 100, 1)

# 创建左右两个子图（1行2列）
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=False)


list_loss = []
list_phase = []
for fre in fres:
    eps, epsH, relationtime = Eps_list[20]    # 假设使用20℃的参数进行计算
    Res, Ims, Loss_tangents = DebyeModel(eps, epsH, relationtime, fre)

    loss_MAG = S21_MAG(Res, Loss_tangents, length=0.1)  # 假设传播距离为0.1米
    phase_PHS = S21_PHS(Res, length=0.1)  # 假设传播距离为0.1米
    list_loss.append(loss_MAG)
    list_phase.append(phase_PHS)

    # 实部子图（左）
ax1.plot(fres, list_phase, label=f"相位延迟", color='red', linewidth=2)

    # 虚部子图（右）
ax2.plot(fres, list_loss, label=f"幅度衰减", color='green', linewidth=2)

# 设置左图（实部）
ax1.set_title("相位差", fontsize=13)
ax1.set_xlabel("频率 / GHz")
ax1.set_ylabel("角度/°")
ax1.grid(True)
ax1.legend()

# 设置右图（虚部）
ax2.set_title("幅度衰减", fontsize=13)
ax2.set_xlabel("频率 / GHz")
ax2.set_ylabel("分贝/dB")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()