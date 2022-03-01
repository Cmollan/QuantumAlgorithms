import math
import cmath


class Sinusoid:
    def __init__(self, func, freq, amp, phase):
        self.func = func
        self.freq = freq
        self.amp = amp
        self.phase = phase


def DiscreteFourierTransform(xk, T):
    epsilon = 1 * 10 ** -4
    N = len(xk)
    y = []
    sample_resolution = T/N

    for n in range(0, N):
        frequency = sample_resolution * n
        sum = 0

        for k in range(0, N):
            alpha = math.cos(
                -(2 * math.pi) / N * k * n
            )
            beta = math.sin(
                -(2 * math.pi) / N * k * n
            )
            sum += xk[k] * (alpha + beta * 1j)

        if frequency <= T/2:
            sum = sum * 2

            [magnitude, phase] = cmath.polar(sum)
            amplitude = magnitude / N

            if abs(amplitude) > epsilon:
                temp_ans = Sinusoid(
                    "cosine",
                    frequency,
                    amplitude,
                    phase
                )
                y.append(temp_ans)

        else:
            return y


xk = []
for i in range(0, 16):
    xk.append(
        math.cos(i * math.pi/2)
        + math.sin(i * math.pi/4)
    )

if __name__ == "main":
    test = DiscreteFourierTransform(xk, 8)
    print(test)
