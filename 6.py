import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a*(time**2) + b*time + c
    return temperature

def main():
    filename = input("Enter the filename containing the coefficients: ")

    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            coefficients = line.split(',')
            a = float(coefficients[0])
            b = float(coefficients[1])
            c = float(coefficients[2])

        time_values = np.linspace(0, 10, 50)

        temperature_values = quadratic_model(time_values, a, b, c)
        plt.plot(time_values, temperature_values, label=f'Single Set (a={a}, b={b}, c={c})')

        plt.xlabel('Time')
        plt.ylabel('Temperature')
        plt.legend()
        plt.title('Single set from file 1.txt')
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


if __name__ == '__main__':
    main()
