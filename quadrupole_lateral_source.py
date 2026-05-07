import matplotlib.pyplot as plt
import numpy as np
import os


def quadrupole_lateral_source():
    ## Quadrupole parameters

    # Radius of each monopole sphere $a$
    a_radius = 0.01

    # Velocity of the surface of each sphere $u$
    u_velocity = 1.0

    # Separation distance between adjacent monopoles $d$
    d_separation = 0.1

    # Surface area of each monopole sphere
    S_area = 4 * np.pi * a_radius**2

    # Volume velocity of each monopole in the quadrupole $Q = S * u$
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

    # Angle in degrees over which the SPL is to be calculated
    theta_deg = np.linspace(0, 360, 720, endpoint=False)

    # Convert to radians
    theta_rad = np.deg2rad(theta_deg)

    # Radius where SPL is to be evaluated
    r_radius = 4  # [m]

    ## Plot

    Q_rms = Q_volume_velocity / np.sqrt(2)

    # Quadrupole acoustic power approximation for four alternating monopoles
    W_Q = (
        (rho_density * c_speed_sound)
        * (
            (k_wavenum**6 * (d_separation / 2) ** 4 * (Q_rms**2))
            / (5 * np.pi * (1 + k_wavenum**2 * a_radius**2))
        )
    )

    # Lateral quadrupole directivity: cancellation at points equidistant from adjacent monopoles
    directivity = np.sin(2 * theta_rad) ** 2

    p_squared = (
        (5 * W_Q * rho_density * c_speed_sound) / (4 * np.pi * r_radius)
    ) * directivity

    # Avoid log(0)
    epsilon = 1e-20

    SPL_quadrupole_lateral = 10 * np.log10(p_squared / p_ref**2 + epsilon)

    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
    ax.plot(theta_rad, SPL_quadrupole_lateral, linewidth=2.0)
    ax.set_rticks([0, 20, 40, 60, 80])

    # Title and grid
    plt.title("Quadrupole Lateral Source", fontsize=14)
    # plt.grid(True, which="both", linestyle="--", linewidth=1.0)

    # Adjust layout to prevent cutting off the labels
    plt.tight_layout()

    # Ensure the 'figures' directory exists
    os.makedirs("figures", exist_ok=True)

    # Save the plot to a file
    plt.savefig(os.path.join("figures", "quadrupole-lateral-source.png"))

    # Display the plot
    plt.show()
