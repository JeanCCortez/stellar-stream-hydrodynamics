import numpy as np
import matplotlib.pyplot as plt

# Configurações de estilo ApJ
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
})

x = np.linspace(-10, 10, 500)

# 1. Perfil Lambda-CDM (Sub-halo Impact com "Epaulets" / Ombros)
cdm_gap = -0.8 * np.exp(-x**2 / 2.0)
cdm_shoulders = 0.25 * np.exp(-(x - 3.5)**2 / 1.5) + 0.25 * np.exp(-(x + 3.5)**2 / 1.5)
density_cdm = 1.0 + cdm_gap + cdm_shoulders
density_cdm += np.random.normal(0, 0.02, size=len(x))

# 2. Perfil Hydrodynamic Shear (Continuity Equation) - REMOVIDO "RRT"
density_hydro = 1.0 - 0.75 * np.exp(-x**2 / 4.0)

fig, ax = plt.subplots(figsize=(8, 4.5))

ax.plot(x, density_cdm, color='#D32F2F', lw=2, label=r'$\Lambda$CDM Sub-halo Impact (N-body)')
# CORREÇÃO APLICADA NA LINHA ABAIXO:
ax.plot(x, density_hydro, color='#1976D2', lw=2.5, label=r'Hydrodynamic Shear (Continuity Eq.)')

# Anotações visuais
ax.annotate('Density Pile-up\n("Epaulets")', xy=(3.5, 1.15), xytext=(5, 1.3),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, ha='center', color='#D32F2F')

ax.annotate('Smooth Expansive Depletion\n(No Edge Clustering)', xy=(2.0, 0.5), xytext=(5, 0.4),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, ha='center', color='#1976D2')

# Linha base (Densidade não perturbada = 1.0)
ax.axhline(1.0, color='black', linestyle=':', lw=1.5, label='Unperturbed Stream Density $\\rho_0$')

ax.set_title('Morphological Density Profiles: N-body vs. Hydrodynamic Fluid', fontweight='bold')
ax.set_xlabel(r'Distance along the Stream $\Delta x$ (kpc)')
ax.set_ylabel(r'Normalized Mass Density $\rho(x)/\rho_0$')
ax.set_ylim(0.1, 1.5)
ax.set_xlim(-10, 10)

ax.legend(loc='lower right', frameon=True, edgecolor='black')
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('figure3_density_profile.pdf', dpi=300, bbox_inches='tight')
print("Figura 3 salva com sucesso! (Sem o termo RRT)")