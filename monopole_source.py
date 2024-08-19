import matplotlib.pyplot as plt
import numpy as np
import os


def monopole_source():
    # Define properties of air and the sound velocity
    rho = 1.21
    c = 343

    ## Define coordinates of wall
    H = 4  # [m] width of wall
    L = H  # [m] length of wall
    W = 1

    ## plot the SPL
    radius = 4
    theta = np.linspace(-180, 180, 360)
    # print('theta: ', theta)

    r = np.cos(theta * np.pi) * radius

    d = np.sin(theta * np.pi) * radius

    h = H / 2

    alpha = H / L
    beta = h / L

    SPL = np.zeros(len(theta))
    # print('SPL: ', SPL)

    for i in range(len(theta)):
        gamma = r[i] / L
        delta = d[i] / L

        p_squared = rho * c * W / (2 * np.pi * H * L)

        # p_squared = rho * c * W / (2 * np.pi * H * L) * (
        #     np.arctan((alpha - beta) * delta + 0.5)
        # )

        SPL[i] = 10 * np.log10(np.abs(p_squared) / (20e-6) ** 2)

    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})

    # Title and grid
    plt.title("Monopole Source", fontsize=14)
    # plt.grid(True, which="both", linestyle="--", linewidth=1.0)

    # Adjust layout to prevent cutting off the labels
    plt.tight_layout()

    # Ensure the 'figures' directory exists
    os.makedirs("figures", exist_ok=True)

    # Save the plot to a file
    plt.savefig(os.path.join("figures", "monopole-source.png"))

    ax.plot(theta * np.pi / 180, SPL)
    ax.set_rticks([0, 20, 40, 60, 80, 100])
    plt.show()
