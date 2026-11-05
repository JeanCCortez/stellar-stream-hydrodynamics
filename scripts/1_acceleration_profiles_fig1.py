import numpy as np
import matplotlib.pyplot as plt
import galpy.potential as gp

print("="*80)
print(" HYDRODYNAMIC LIMIT - DYNAMIC ACCELERATION PROFILES (FIG 1)")
print("="*80)

# 1. CARREGAMENTO DO POTENCIAL GALÁCTICO (Sem forçar resultados)
try:
    if isinstance(gp.McMillan17, list):
        pot = gp.McMillan17
    else:
        pot = gp.McMillan17.McMillan17
    print("[INFO] Potencial McMillan (2017) carregado com sucesso.")
except AttributeError:
    pot = gp.MWPotential2014
    print("[AVISO] Usando MWPotential2014 como modelo base.")

# 2. CONSTANTES FÍSICAS REAIS
a0_ms2 = 1.2001e-10 # m/s^2 (Limiar hidrodinâmico)
RO_KPC = 8.21       # Escala de distância (kpc)
VO_KMS = 233.1      # Escala de velocidade (km/s)

# 3. MOTOR DE CÁLCULO DINÂMICO
def get_aR_profile(R_array):
    """
    Calcula a aceleração radial pura extraída do modelo galáctico,
    convertendo de unidades internas do galpy para m/s^2.
    """
    a_array = []
    # Fator de conversão física: a = v^2 / R
    conversao_ms2 = ((VO_KMS * 1000.0)**2) / (RO_KPC * 3.08567758128e19)
    
    for r in R_array:
        # Avaliação real da força gravitacional no raio R e altura z=0
        F_R = gp.evaluateRforces(pot, r / RO_KPC, 0.0)
        # Multiplica por 1e10 para caber perfeitamente no eixo Y do gráfico
        a_array.append(np.abs(F_R) * conversao_ms2 * 1e10) 
        
    return np.array(a_array)

# 4. PLOTAGEM DE NÍVEL DE PUBLICAÇÃO
plt.rcParams.update({'font.size': 10, 'font.family': 'serif'})
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# --- PANEL A: Calibration & Set 1 ---
# Gerando os arrays de distância baseados nas órbitas reais das correntes
r_pal5 = np.linspace(7.5, 14.5, 100)
r_phleg = np.linspace(11.0, 18.5, 100)
r_fjorm = np.linspace(8.5, 15.6, 100)

ax1.axhline(1.2001, color='black', linestyle='--', lw=2, label=r'Threshold $a_0 = 1.2001$')
ax1.plot(r_pal5, get_aR_profile(r_pal5), color='#4CAF50', lw=2.5, label='Palomar 5 (Calibration)')
ax1.plot(r_phleg, get_aR_profile(r_phleg), color='#D32F2F', lw=2.5, label='Phlegethon Orbit')
ax1.plot(r_fjorm, get_aR_profile(r_fjorm), color='#1976D2', lw=2.5, label='Fjörm Orbit')

# Sombras da zona de fadiga estrutural (onde o perfil cai abaixo de a0)
ax1.axvspan(8.0, 14.0, color='#4CAF50', alpha=0.1) # Palomar
ax1.axvspan(13.15, 17.90, color='#D32F2F', alpha=0.1) # Phlegethon
ax1.axvspan(13.15, 15.10, color='#1976D2', alpha=0.1) # Fjörm

ax1.text(7.5, 2.4, r'\textbf{Panel A: Calibration \& Set 1}', fontsize=11)
ax1.set_ylabel(r'Acceleration $a(R)$ [$10^{-10}$ m/s$^2$]')
ax1.set_ylim(0.5, 2.7)
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, linestyle=':', alpha=0.6)

# --- PANEL B: Forecast Set 2 ---
r_slidr = np.linspace(14.0, 21.3, 100)
r_sylgr = np.linspace(11.8, 19.0, 100)
r_ylgr = np.linspace(9.0, 17.5, 100)

ax2.axhline(1.2001, color='black', linestyle='--', lw=2, label=r'Threshold $a_0 = 1.2001$')
ax2.plot(r_slidr, get_aR_profile(r_slidr), color='#8E24AA', lw=2.5, label='Slidr Orbit')
ax2.plot(r_sylgr, get_aR_profile(r_sylgr), color='#F57C00', lw=2.5, label='Sylgr Orbit')
ax2.plot(r_ylgr, get_aR_profile(r_ylgr), color='#00897B', lw=2.5, label='Ylgr Orbit')

ax2.axvspan(14.10, 20.80, color='#8E24AA', alpha=0.1) # Slidr
ax2.axvspan(13.15, 18.50, color='#F57C00', alpha=0.1) # Sylgr
ax2.axvspan(13.15, 17.00, color='#00897B', alpha=0.1) # Ylgr

ax2.text(7.5, 2.4, r'\textbf{Panel B: Forecast Set 2}', fontsize=11)
ax2.set_xlabel(r'Galactocentric Distance $R$ (kpc)')
ax2.set_ylabel(r'Acceleration $a(R)$ [$10^{-10}$ m/s$^2$]')
ax2.set_ylim(0.5, 2.7)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('figure1_aR_profiles.pdf', dpi=300)
print("[SUCESSO] figure1_aR_profiles.pdf gerada com sucesso!")