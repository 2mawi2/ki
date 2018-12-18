def y(x):
    return ((x ** 3) / 3) + 50 * x ** 2 - 100 * x - 30


def gradient_descent(gradient, start, alpha) -> float:
    current_x = start
    precision = 0.000001
    previous_step_size = 1
    max_iterations = 10000
    iteration_counter = 0

    while previous_step_size > precision and iteration_counter < max_iterations:
        previous_x = current_x  # store x of previous iteration
        current_x = current_x - alpha * gradient(previous_x)  # actual gradient descent
        previous_step_size = abs(current_x - previous_x)  # store previous step size (difference in x)
        iteration_counter += 1
        print(f"Iteration: {iteration_counter} with x: {current_x} with value {y(current_x)}")

    return current_x


if __name__ == '__main__':
    local_minimum = gradient_descent(
        gradient=y,
        start=3,
        alpha=0.01)

    print(f"Local minimum found at: {local_minimum} with value {y(local_minimum)}")
