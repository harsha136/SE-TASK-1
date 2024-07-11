import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time):
    a = 0.1
    b = -1
    c = 30

    temperature = a*(time**2) + b*time + c
    return temperature

def main():
    time_values = np.linspace(0, 10, 50)

    temperature_values = quadratic_model(time_values)
    plt.plot(time_values,temperature_values,label='Hard Coded Coefficient')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Quadratic equation with hard coded coefficient')
    plt.show()


if __name__ == '__main__':
    main()
