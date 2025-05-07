import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from sympy import primepi
import csv

# ===== Step 1: 构造真实素数密度 π(x)/x =====
x_vals = np.linspace(100, 10000, 500)
pi_x = np.array([primepi(int(x)) for x in x_vals])
pi_norm = pi_x / x_vals

# ===== Step 2: 选取 ζ 零点作为模态频率 tn =====
t_n = np.array([
    14.13472514, 21.02203964, 25.01085758, 30.42487613, 32.93506159,
    37.58617816, 40.91871901, 43.32707328, 48.00515088, 49.77383248,
    52.97032148, 56.4462477, 59.347044, 60.83177852, 65.11254405
])
N = len(t_n)

# ===== Step 3: 定义模型频率函数 rho(x) =====
def rho_model(x, A, theta):
    rho = 1 / np.log(x)
    for n in range(N):
        rho += A[n] * np.cos(t_n[n] * np.log(x) + theta[n])
    return rho

# ===== Step 4: 定义优化目标（残差 δ²） =====
def cost(params, x, target):
    A = params[:N]
    theta = params[N:]
    rho_vals = rho_model(x, A, theta)
    return np.mean((rho_vals - target) ** 2)

# ===== Step 5: 初始化并优化 =====
A_init = np.ones(N) * 0.01
theta_init = np.linspace(0, 2*np.pi, N)
params_init = np.concatenate([A_init, theta_init])
bounds = [(0, 0.1)] * N + [(0, 2*np.pi)] * N

result = minimize(cost, params_init, args=(x_vals, pi_norm), method='L-BFGS-B', bounds=bounds)

# ===== Step 6: 提取参数并重构结构 =====
A_opt = result.x[:N]
theta_opt = result.x[N:]
rho_opt = rho_model(x_vals, A_opt, theta_opt)
delta_sq_proj = np.mean((rho_opt - pi_norm) ** 2)

# ===== Step 7: 控制台输出结果 =====
print(f"\n✅ NHSN ζ 投影拟合完成")
print(f"Final projection error δ² = {delta_sq_proj:.6f}")
print("—" * 50)

# ===== Step 8: 绘图（不保存图像文件） =====
plt.figure(figsize=(12, 4))
plt.plot(x_vals, pi_norm, label='π(x)/x (True)', lw=2)
plt.plot(x_vals, rho_opt, label='ρ(x) (Zeta-based projection)', lw=2, linestyle='--')
plt.title("ζ-Based Modal Projection Reconstructing π(x)/x")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ===== Step 9: 导出 CSV 参数文件 =====
with open("modal_projection_parameters.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ζ-zero t_n", "A_n (Amplitude)", "θ_n (Phase in rad)"])
    for tn_i, a_i, th_i in zip(t_n, A_opt, theta_opt):
        writer.writerow([f"{tn_i:.6f}", f"{a_i:.6f}", f"{th_i:.6f}"])
print("✅ 模态参数保存为：modal_projection_parameters.csv")

# ===== Step 10: 打印 LaTeX 表格片段（前5项） =====
print("\n📝 LaTeX 表格片段（Top 5 模态）:")
print(r"\begin{tabular}{c|c|c}")
print(r"$t_n$ & $A_n$ & $\theta_n$ \\ \hline")
for i in range(min(5, len(t_n))):
    print(f"{t_n[i]:.4f} & {A_opt[i]:.5f} & {theta_opt[i]:.4f} \\\\")
print(r"\end{tabular}")

# ===== Step 11: StructureLang ψ-path 表达 =====
print("\n🧠 StructureLang ψ-paragraph:")
active_modes = [i for i in range(len(A_opt)) if A_opt[i] > 0.005]
psi_path = " ⊕ ".join([f"ψ{n+1}" for n in active_modes])
x_start, x_end = int(x_vals[0]), int(x_vals[-1])
print(f"ψ-paragraph := {psi_path} ⊂ x ∈ [{x_start}, {x_end}]")