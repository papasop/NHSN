# HPO2: Non-Hermitian Spectral Network for Prime Structure Reconstruction

This project implements a frequency-based spectral model (HPO2) that reconstructs the prime density function π(x)/x using the first N Riemann zeta zeros as modal frequencies. Based on the theory of Non-Hermitian Spectral Networks (NHSN), this approach interprets Riemann zeros as frequency-locking resonance points in a dynamic spectral field.

---

## 📘 Core Idea

We model the prime density structure as a modal frequency projection:

\[
\rho(x) = \frac{1}{\log x} + \sum_{n=1}^{N} A_n \cos(t_n \log x + \theta_n)
\]

Where:
- \( t_n \) = imaginary parts of the first N Riemann zeta zeros (ζ zeros)
- \( A_n \), \( \theta_n \) = optimized modal amplitudes and phases
- ρ(x) ≈ π(x)/x when parameters are optimized

---

## 💡 Why HPO2?

| Feature               | Traditional HPO             | HPO2 / NHSN                          |
|----------------------|-----------------------------|--------------------------------------|
| ζ zeros              | Static eigenvalues          | Emergent modal resonances            |
| Operator type        | Hermitian (self-adjoint)    | Non-Hermitian (asymmetric kernel)    |
| Spacing              | Linear / Regular            | GUE-like, irregular                  |
| Information          | Not transmittable           | ψ-paths can encode structured info   |
| Output               | Real λₙ ~ tₙ²               | √λₙ ~ tₙ + δ(x)                      |

---

## 🧠 What This Code Does

- ✅ Loads prime density data π(x)/x via `sympy.primepi`
- ✅ Uses the first 15 Riemann ζ zeros as modal frequencies \( t_n \)
- ✅ Optimizes \( A_n \), \( \theta_n \) using L-BFGS-B
- ✅ Computes modal projection ρ(x)
- ✅ Measures reconstruction accuracy via MSE (δ²)
- ✅ Outputs:
  - Matplotlib plot of ρ(x) vs π(x)/x
  - CSV table of modal parameters
  - LaTeX table for reports
  - StructureLang ψ-paragraph

---

## 📂 Files

| File                      | Description                                 |
|---------------------------|---------------------------------------------|
| `hpo2.py`                 | Main script to perform modal fitting        |
| `modal_projection_parameters.csv` | Output CSV of \( t_n, A_n, \theta_n \)       |
| `projection_result.png`   | Visual comparison (if saved)                |
| `README.md`               | This file                                   |

---

## ▶️ How to Run

```bash
pip install numpy matplotlib scipy sympy
python3 hpo2.py







