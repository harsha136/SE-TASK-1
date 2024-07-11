import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a*(time**2) + b*time + c
    return temperature

def main():
    a = float(input("Enter the value of coefficient a: "))
    b = float(input("Enter the value of coefficient b: "))
    c = float(input("Enter the value of coefficient c: "))

    time_values = np.linspace(0, 10, 50)

    temperature_values = quadratic_model(time_values, a, b, c)
    plt.plot(time_values, temperature_values, label=f'Set (a={a}, b={b}, c={c})')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('User Input')
    plt.show()

if __name__ == '__main__':
    main()
