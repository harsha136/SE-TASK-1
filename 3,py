import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a*(time**2) + b*time + c
    return temperature

def main():
    coefficient_sets = [
        (2, 1, 30),
        (2, -2, 40),
        (4, -3, 50),
    ]

    time_values = np.linspace(0, 10, 50)

    for a, b, c in coefficient_sets:
        temperature_values = quadratic_model(time_values, a, b, c)
        plt.plot(time_values, temperature_values, label=f'set (a={a}, b={b}, c={c})')

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Multiple sets')
    plt.show()

if __name__ == '__main__':
    main()
