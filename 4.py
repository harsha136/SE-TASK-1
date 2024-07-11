import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a*(time**2) + b*time + c
    return temperature

def main():
    filename = input("Enter the filename containing the coefficient sets: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        num_sets = len(lines)

        a_values = []
        b_values = []
        c_values = []

        for line in lines:
            coefficients = line.strip().split(',')
            a = float(coefficients[0])
            b = float(coefficients[1])
            c = float(coefficients[2])
            a_values.append(a)
            b_values.append(b)
            c_values.append(c)

        time_values = np.linspace(0, 10, 50)

        for i in range(num_sets):
            temperature_values = quadratic_model(time_values, a_values[i], b_values[i], c_values[i])
            plt.plot(time_values, temperature_values, label=f'SET (a={a_values[i]}, b={b_values[i]}, c={c_values[i]})')

        plt.xlabel('Time')
        plt.ylabel('Temperature')
        plt.legend()
        plt.title('Multiple sets from file 2.txt')
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


if __name__ == '__main__':
    main()
