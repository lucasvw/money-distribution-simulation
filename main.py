import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

amount_of_people = 100

n = amount_of_people - 1
p = 1 / n
start_money = 100

bank = start_money*np.ones([amount_of_people])

range = np.arange(amount_of_people)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

bar = plt.bar(range,bank)

def init():
    return bar

def animate(i):
    global bank, ax
    bank = bank + np.random.binomial(n, p, amount_of_people) - 1
    bank[bank<0] = 0
    bank = np.sort(bank)
    for rect, y in zip(bar, bank):
        rect.set_height(y)
    ax.set_ylim(0,max(bank))
    ax.set_title(i)
    return bar

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1500, interval=1, blit=False)

plt.show()