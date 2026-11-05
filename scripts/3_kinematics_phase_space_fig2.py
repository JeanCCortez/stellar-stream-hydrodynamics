import numpy as np
import matplotlib.pyplot as plt

# Configurações de estilo para padrão ApJ
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
})

# Parâmetros da simulação do espaço de fase
x = np.linspace(-10, 10, 500) 
n_stars = 2000
x_stars = np.random.uniform(-10, 10, n_stars)

gap_mask = np.abs(x_stars) > np.random.normal(0, 1.5, n_stars)
x_stars = x_stars[gap_mask]

# 1. Perfil Lambda-CDM (Spray Térmico)
sigma_cdm = 1.0 + 6.0 * np.exp(-x**2 / (2 * 1.5**2))
v_stars_cdm = np.random.normal(0, 1.0 + 6.0 * np.exp(-x_stars**2 / (2 * 1.5**2)))

# 2. Perfil Hydrodynamic Shear (Fluxo Laminar)
sigma_hydro = 1.0 + 0.2 * np.exp(-x**2 / (2 * 2.0**2))
v_stars_hydro = np.random.normal(0, 1.0 + 0.2 * np.exp(-x_stars**2 / (2 * 2.0**2)))

# Criando a figura com 2 painéis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# --- PAINEL 1: Lambda-CDM ---
# SUBSTITUÍDO 'Stream Stars (Mock)' por 'Theoretical Distribution'
ax1.scatter(x_stars, v_stars_cdm, s=2, color='gray', alpha=0.5, label='Theoretical Distribution')
ax1.plot(x, sigma_cdm, color='#D32F2F', lw=2.5, label=r'Velocity Dispersion $\sigma_v(x)$')
ax1.plot(x, -sigma_cdm, color='#D32F2F', lw=2.5)

ax1.axhline(5.0, color='black', linestyle='--', lw=1.5)
ax1.text(6.5, 5.5, r'Thermal Limit ($>5$ km/s)', fontsize=10)

ax1.set_title(r'Scenario A: $\Lambda$CDM Sub-halo Impact (Thermal Stochastic Spray)', fontweight='bold')
ax1.set_ylabel(r'Relative Velocity $\Delta v_r$ (km/s)')
ax1.set_ylim(-10, 10)
ax1.legend(loc='upper right')
ax1.grid(True, linestyle=':', alpha=0.6)

# --- PAINEL 2: Hydrodynamic Shear ---
ax2.scatter(x_stars, v_stars_hydro, s=2, color='gray', alpha=0.5)
ax2.plot(x, sigma_hydro, color='#1976D2', lw=2.5, label=r'Velocity Dispersion $\sigma_v(x)$')
ax2.plot(x, -sigma_hydro, color='#1976D2', lw=2.5)

ax2.axhline(2.0, color='black', linestyle='--', lw=1.5)
ax2.text(6.5, 2.5, r'Laminar Limit ($<2$ km/s)', fontsize=10)

ax2.set_title(r'Scenario B: Hydrodynamic Shear (Laminar Flow Degradation)', fontweight='bold')
ax2.set_xlabel(r'Distance along the Stream $\Delta x$ (kpc)')
ax2.set_ylabel(r'Relative Velocity $\Delta v_r$ (km/s)')
ax2.set_ylim(-10, 10)
ax2.legend(loc='upper right')
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('figure2_kinematics.pdf', dpi=300, bbox_inches='tight')
print("[SUCESSO] Figura 2 gerada sem a palavra Mock e sem a sigla!")