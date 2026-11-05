import numpy as np
from scipy.stats import binom

print("="*60)
print(" STELLAR STREAMS - BINOMIAL PROBABILITY AUDIT")
print("="*60)

n_streams = 5  
p_random = 0.16  

print(f"Number of forecast targets: {n_streams}")
print(f"Probability of random alignment per stream: {p_random}\n")
print("Successful Alignments (k) | Confidence (1-p) | Verdict")
print("-" * 60)

for k in range(3, 6):
    p_value = 1.0 - binom.cdf(k - 1, n_streams, p_random)
    confidence = (1.0 - p_value) * 100
    
    if k == 3: verdict = "> 2 sigma detection"
    elif k == 4: verdict = "> 3 sigma detection"
    else: verdict = "> 4 sigma discovery"
        
    print(f"k >= {k}                   | {confidence:.2f}%         | {verdict}")
print("="*60)