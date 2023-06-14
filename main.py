import numpy as np
import matplotlib.pyplot as plt

a = 0
b = np.pi
N = 1000

ar = np.zeros(N)

for i in range(len(ar)):
    ar[i] = np.random.uniform(a, b)

integral = 0.0

def f(x):
    return np.sin(x)

for i in ar:
    integral += f(i)

ans = (b - a) / float(N) * integral
x = np.linspace(a, b, 100)
y = f(x)

# Plotting the points and the function
plt.figure(figsize=(8, 6))
plt.scatter(ar, np.zeros_like(ar), color='blue', alpha=0.6, label='Samples')
plt.plot(x, y, color='red', label='f(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Интеграция по методу Монте-Карло')
plt.legend()
plt.show()

print("Значение, вычисленное методом интегрирования по методу Монте-Карло, равно {}.".format(ans))
