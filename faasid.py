import numpy as np
import matplotlib.pyplot as plt

# Konstandid
f = 78e6  # Hz
c = 3e8   # m/s
mu = 4 * np.pi * 1e-7  # N/A^2
sigma = 3.77e7  # S/m
d_foil = 0.016e-3  # m

# Arvutused
alpha = (sigma / 2) * np.sqrt(mu * sigma / 2)
A = alpha * d_foil

# Fooliumi paksuse ulatus
z_values = np.linspace(0, d_foil, 1000)

# Elektrivälja amplituudi ja faasi arvutused
E_amplitude = 30 * np.exp(-A * z_values)
phi = -alpha * z_values

# Graafikute joonistamine
plt.figure(figsize=(10, 6))

# Elektrivälja amplituudi graafik
plt.subplot(2, 1, 1)
plt.plot(z_values, E_amplitude)
plt.title('Elektrivälja amplituudi graafik')
plt.xlabel('Fooliumi kaugus (m)')
plt.ylabel('Elektrivälja amplituud (V/m)')

# Faasi graafik
plt.subplot(2, 1, 2)
plt.plot(z_values, phi)
plt.title('Faasi graafik')
plt.xlabel('Fooliumi kaugus (m)')
plt.ylabel('Faas (rad)')

plt.tight_layout()
plt.show()
