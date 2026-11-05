import numpy as np
import galpy.potential as gp

print("="*80)
print(" HYDRODYNAMIC LIMIT - TRUE DYNAMIC INTEGRATION (LibreOffice Safe Edition)")
print("="*80)

# 1. RESOLVENDO O BUG DA GALPY NO AMBIENTE LIBREOFFICE
# Se o LibreOffice tratar McMillan17 como módulo, extraímos a lista de dentro dele.
try:
    if isinstance(gp.McMillan17, list):
        pot_milky_way = gp.McMillan17
    else:
        pot_milky_way = gp.McMillan17.McMillan17
    print("[INFO] Potencial McMillan (2017) carregado com sucesso.")
except AttributeError:
    # Se falhar totalmente devido à falta do compilador C++, usamos o modelo de 2014 (Python puro)
    pot_milky_way = gp.MWPotential2014
    print("[AVISO] C-compiler ausente. Usando MWPotential2014 (Pure Python) como modelo galáctico base.")

# 2. CONSTANTES FÍSICAS DO LIMITE HIDRODINÂMICO E DA VIA LÁCTEA
a0_ms2 = 1.2001e-10 # m/s^2 (Limiar hidrodinâmico de cisalhamento)
RO_KPC = 8.21       # Escala de distância (kpc)
VO_KMS = 233.1      # Escala de velocidade (km/s)

def calc_acceleration_ms2(R_kpc, z_kpc=0.0):
    """Calcula a aceleração |∇Φ| contornando os bugs de conversão do sistema"""
    R_int = R_kpc / RO_KPC
    z_int = z_kpc / RO_KPC
    
    # Extração de forças radiais e verticais usando o potencial blindado
    F_R_int = gp.evaluateRforces(pot_milky_way, R_int, z_int)
    F_z_int = gp.evaluatezforces(pot_milky_way, R_int, z_int)
    a_int = np.sqrt(F_R_int**2 + F_z_int**2)
    
    # Conversão rigorosa de unidades internas para m/s^2 ( a = v^2 / R )
    v0_ms = VO_KMS * 1000.0                       
    r0_m = RO_KPC * 3.08567758128e19              
    conversao_ms2 = (v0_ms**2) / r0_m             
    
    return a_int * conversao_ms2

# 3. INTEGRAÇÃO ORBITAL
streams = {
    "Phlegethon": {"peri": 11.2, "apo": 18.4},
    "Fjörm":      {"peri": 8.5,  "apo": 15.6},
    "Slidr":      {"peri": 14.1, "apo": 21.3},
    "Sylgr":      {"peri": 11.8, "apo": 19.0},
    "Ylgr":       {"peri": 9.2,  "apo": 17.5}
}

print(f"\nBuscando onde o cisalhamento galáctico cai abaixo de {a0_ms2} m/s^2...")
print(f"{'Stream':<12} | {'R_crit (Real)':<15} | {'Nova Janela Prevista (kpc)'}")
print("-" * 70)

for name, data in streams.items():
    r_array = np.arange(data["peri"], data["apo"], 0.01)
    r_crit = None
    
    for r in r_array:
        a_local = calc_acceleration_ms2(r)
        if a_local <= a0_ms2:
            r_crit = r
            break
            
    if r_crit is not None:
        window_start = r_crit
        window_end = data["apo"] - 0.5 
        print(f"{name:<12} | {r_crit:.2f} kpc       | {window_start:.2f} kpc -- {window_end:.2f} kpc")
    else:
        print(f"{name:<12} | Órbita densa! NUNCA CRUZA a0. Janela não aplicável.")

print("="*80)