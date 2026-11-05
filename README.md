# Stellar Stream Hydrodynamics: Gap Forecasting Framework

This repository contains the dynamic integration scripts and empirical validation data supporting the research article: **"Deterministic Morphological Forecasts for Galactic Stellar Streams: A Universal Hydrodynamic Limit Signature for Upcoming LSST and Gaia Observations."**

## Overview
This framework models the structural fatigue and subsequent morphological ruptures (gaps) of cold stellar streams in the Galactic halo using a macroscopic fluid dynamics approach. By applying a universal acceleration threshold ($a_0 = 1.2001 \times 10^{-10} \, \mathrm{m \, s^{-2}}$), the code computes the exact galactocentric windows where the cosmic vacuum acts as a dissipative medium, eliminating the need to invoke stochastic dark matter sub-halo collisions.

## Repository Contents

### 1. Dynamic Forecasts & Orbit Integration
*   `1_acceleration_profiles_fig1.py`: Plots dynamic acceleration profiles $a(R)$ across galactocentric distances, mapping the threshold crossing for eccentric orbits.
*   `2_forecast_calculator_table2.py`: The core `galpy` integration engine. Computes the exact rupture windows for five unmapped streams (Phlegethon, Fjörm, Slidr, Sylgr, Ylgr) based on the `MWPotential2014` background.

### 2. Empirical Validation (Gaia EDR3)
*   `asu.tsv`: Raw astrometric catalog of the Sloan Stream (GD-1) from Gaia EDR3 (Ibata et al. 2021).
*   `4_sloan_density_REAL.py`: Processes the `asu.tsv` catalog to isolate real Sloan members, computes their galactocentric distances, and overlays the macroscopic Hydrodynamic Shear Model curve to validate the density gap without N-body perturbers.

### 3. Theoretical Discriminators (Future Surveys)
*   `3_kinematics_phase_space_fig2.py`: Simulates the predicted 6D phase-space signatures, distinguishing between the thermal stochastic spray of $\Lambda$CDM ($> 5 \, \mathrm{km/s}$) and the laminar flow of hydrodynamic shear ($< 2 \, \mathrm{km/s}$).
*   `5_morphological_density_fig3.py`: Visualizes the 1D continuity equation, contrasting smooth expansive depletion against the density pile-ups ("epaulets") expected from elastic sub-halo impacts.

### 4. Statistical Falsifiability
*   `6_binomial_statistics_table3.py`: Calculates the binomial probabilities of random gap alignments, establishing the $>3\sigma$ threshold for rejecting the stochastic null hypothesis based on upcoming Gaia DR4 and LSST observations.

## Reproducibility
All Python scripts are self-contained. The empirical validation (`4_sloan_density_REAL.py`) requires the `asu.tsv` file to be in the same directory.
Dependencies: `numpy`, `pandas`, `matplotlib`, `astropy`, `galpy`, `scipy`.
