import matplotlib.pyplot as plt
import numpy as np


def T(t):
    return 22.5 + 57.5 * np.e ** (-0.023 * t)


def beregn_tid_for_onsket_temp(ønsket_T):
    """Beregner antall minutt det tar før kakaoen når den ønskede temperaturen"""
    d = 0.005
    venstre = 0
    høyre = 100

    while True:
        midtpunkt = (venstre + høyre) / 2
        if ønsket_T + d > T(midtpunkt) > ønsket_T - d:
            return midtpunkt
        elif T(midtpunkt) > ønsket_T:
            venstre = midtpunkt
        else:
            høyre = midtpunkt


def plott():
    # teoretiske verdier
    x = np.linspace(0, 72, 1000)
    temperatur = T(x)

    # mine målinger
    x_eksperimentell = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        10,
        11,
        12,
        14,
        18,
        21,
        23,
        27,
        30,
        37,
        44,
        49,
        54,
        57,
        64,
        72,
    ]
    temperatur_eksperimentell = [
        80,
        79.6,
        77.9,
        74.7,
        75.4,
        71.5,
        69.4,
        66.9,
        62.3,
        61.9,
        61.2,
        58.4,
        54.4,
        52.0,
        51.1,
        48.4,
        46.6,
        42.8,
        40.5,
        39.3,
        38.1,
        37.1,
        35.7,
        34,
    ]

    plt.plot(x, temperatur, label="Teoretisk T endring")
    plt.plot(x_eksperimentell, temperatur_eksperimentell, label='Eksperimentell -"-')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    print(
        f"Antall minutter for at kakaoen skal bli 50 grader: {beregn_tid_for_onsket_temp(50)} min"
    )
    plott()
