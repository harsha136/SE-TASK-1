import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a*(time**2) + b*time + c
    return temperature

def main():
    time_values = np.linspace(0, 10, 50)

    a_hc = 22
    b_hc = -8
    c_hc = 18

    a_user = float(input("Enter the value for coeff a: "))
    b_user = float(input("Enter the value for coeff b: "))
    c_user = float(input("Enter the value for coeff c: "))

    temperature_hard = quadratic_model(time_values, a_hc, b_hc, c_hc)
    plt.plot(time_values, temperature_hard, label=f'Hard Coded Coefficient (a={a_hc}, b={b_hc}, c={c_hc})')

    temperature_user = quadratic_model(time_values, a_user, b_user, c_user)
    plt.plot(time_values, temperature_user, label=f'User Input COefficient (a={a_user}, b={b_user}, c={c_user})')

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Quadratic equation with hard-coded and user input coefficients')
    plt.show()

if __name__ == '__main__':
    main()
