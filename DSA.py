import matplotlib.pyplot as plt
import numpy as np

# Define functions for each problem
def problem_1(x):
    return x**2 + 7 + 2

def problem_2(x):
    return 3*x + 2

def problem_3(x):
    return x**2

def problem_4(x):
    return x**3

def problem_5(x):
    return x**5

def problem_6(x):
    return x**3 + 2*x**2 + x + 10

def problem_7(x):
    return x**4 - 3*x**3 + 2*x**2 - x + 11

def problem_8(x):
    return np.sin(x)

def problem_9(x):
    return np.cos(x)

def problem_10(x):
    return x**5 + 4*x**4 + x**3 - 2*x**2 + 100

# Create a list of x values from 1 to 50
x_values = list(range(1, 51))

# Define a function to solve a given problem for all x values
def solve_problem(problem_number):
    if problem_number == 1:
        return [problem_1(x) for x in x_values]
    elif problem_number == 2:
        return [problem_2(x) for x in x_values]
    elif problem_number == 3:
        return [problem_3(x) for x in x_values]
    elif problem_number == 4:
        return [problem_4(x) for x in x_values]
    elif problem_number == 5:
        return [problem_5(x) for x in x_values]
    elif problem_number == 6:
        return [problem_6(x) for x in x_values]
    elif problem_number == 7:
        return [problem_7(x) for x in x_values]
    elif problem_number == 8:
        return [problem_8(x) for x in x_values]
    elif problem_number == 9:
        return [problem_9(x) for x in x_values]
    elif problem_number == 10:
        return [problem_10(x) for x in x_values]
    else:
        print("Invalid problem number")

# Define a function to plot the graph of a given problem
def plot_graph(y_values, problem_number):
    plt.plot(x_values, y_values)
    plt.title("Problem {}".format(problem_number))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

# Define a function to save the results to a text file
def save_to_file(results, problem_number):
    with open("problem_{}.txt".format(problem_number), "w") as file:
        for i, result in enumerate(results):
            file.write("x={}, y={}\n".format(x_values[i], result))

# Main function
def main():
    while True:
        print("Choose a problem to solve (1-10), or enter 11 to show all graphs:")
        choice = int(input())
        if choice == 11:
            for i in range(1, 11):
                y_values = solve_problem(i)
                plot_graph(y_values, i)
                save_to_file(y_values, i)
        elif 1 <= choice <= 10:
            y_values = solve_problem(choice)
            plot_graph(y_values, choice)
            save_to_file(y_values, choice)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()