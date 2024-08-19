import matplotlib.pyplot as plt
import numpy as np
import os

def dipole_source():
    ## Dipole parameters

    # Radius of the dipole sphere $a$
    a_radius = 0.01

    # Velocity of the surface of the sphere $u$
    u_velocity = 1.0

    # Separation distance between the out-of-phase monopoles $d$
    d_separation = 0.1

    # Surface area of each monopole sphere
    S_area = 4 * np.pi * a_radius**2

    # Volume velocity of each monopole in the dipole $Q = S * u$
    Q_volume_velocity = S_area * u_velocity

    ## Fluid parameters

    # Density of the fluid $\rho$
    rho_density = 1.2041

    # Speed of sound of the fluid $c$
    c_speed_sound = 343.024

    # Reference Sound Pressure $p_{\rm{ref}}$
    p_ref = 20e-6

    ## Analysis configuration

    # Harmonic frequency of analysis

    freq = 500
    omega = 2 * np.pi * freq
    k_wavenum = omega / c_speed_sound

    # Angle over which the SPL is to be calculated $\theta$.

    theta = np.linspace(-180, 180, 360)
    print('len theta: ', len(theta))

    # Radius where SPL is to be evaluated
    r_radius = 4 # [m]

    ## Plot

    Q_rms = Q_volume_velocity / np.sqrt(2)

    W_D = (rho_density * c_speed_sound) * ((k_wavenum**4 * (d_separation / 2)**2 * (Q_rms**2)) / (3 * np.pi * (1 + k_wavenum**2 * a_radius**2)))


    p_squared = (3 * W_D * rho_density * c_speed_sound) / (4 * np.pi * r_radius) * np.cos(theta * np.pi / 180)**2

    SPL_dipole = 10 * np.log10(p_squared / p_ref**2)
    # print('SPL: ', SPL_dipole)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta*np.pi/180, SPL_dipole)
    ax.set_rticks([0, 20, 40, 60, 80]) 

    # Title and grid
    plt.title("Dipole Source", fontsize=14)
    # plt.grid(True, which="both", linestyle="--", linewidth=1.0)

    # Adjust layout to prevent cutting off the labels
    plt.tight_layout()

    # Ensure the 'figures' directory exists
    os.makedirs("figures", exist_ok=True)

    # Save the plot to a file
    plt.savefig(os.path.join("figures", "dipole-source.png"))

    # Display the plot
    plt.show()
