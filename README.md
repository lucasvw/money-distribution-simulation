# money-distribution-simulation
Simulates the way money gets distributed if n people give 1 dollar each round to a random person


[SEE HERE][2]

This morning I saw a tweet mentioning an [article][1] with the exciting title:

**Counterintuitive problem: Everyone in a room keeps giving dollars to random others. You’ll never guess what happens next**

So naturally, I was quite excited and wanted to see what happens next! The problem under consideration is:

*Imagine a room full of 100 people with 100 dollars each. With every tick of the clock, every person with money gives a dollar to one randomly chosen other person. After some time progresses, how will the money be distributed?*

Dan Goldstein, writer of the [article][1] argues that many people believe that the money gets more or less evenly distributed. Sometimes you get some, sometimes you lose some, that's the idea.

Turns out, this is not really the case (or actually *really not*). To show this, Dan Goldstein made a simulation in R and a movie to show the results. What you see is the amount of money each person has for each round. The bottom figure is the interesting one, individuals (on the x-axis) are sorted by the amount of money they possess, so you can actually see the distribution of the money as time passes.

{%raw%}
<video width="640" height="400" controls preload> 
    <source src="http://www.decisionsciencenews.com/wp-content/uploads/2017/06/dollar_stacked2.mp4?_=1"></source> 
</video>
{% endraw %}

This simulation is based on people randomly chosing a person to give their dollar to and then summing it all up. It is thus an exact simulation. I was wondering if I could come up with a simulation based on statistics.

Here is my train of thought:

- Each player gives 1 dollar away each round.
- Each player will receive either 0, 1, 2, ... or $$n - 1$$ (with $$n$$ players) dollar each round.
- There are $$n - 1$$ other players, so player $$i$$ gives a dollar to player $$j$$ with probability $$p = 1/(n-1)$$
- Then, the amount of money each player will receive is a random variable following the binomial distribution. Since the binomial distribution is the discrete probability distribution of the number of successes in a sequence of n independant experiments.

{% raw %}
\begin{align}
	\Pr(X = k) = {n \choose k}p^k(1-p)^{n-k}
\end{align}
{% endraw %}

- Now we can draw $$n$$ samples from this distribution to denote the amount of money each player obtains in a single round.

However, there is no guarentee that the sum of these samples actually amounts to the number of money that is being circulated each round ($$n$$ players $$\times 1$$ dollar = $$n$$ dollar). 
Nonetheless, we know the mean of the binomial distribution equals $$np$$ => $$(n-1)*\frac{1}{n-1} = 1$$. So each player is expected to gain a single dollar each round. Because this is also the amount each person gives away, the *expected* amount of money in the game will remain constant. For now, I am quite okay with this assumption.

The following video shows a single *game* with 5000 *rounds*:

{%raw%}
<video width="640" height="400" controls preload> 
    <source src="/assets/videos/money.mp4"></source> 
</video>
{% endraw %}


{% highlight python %}
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
    bank = np.sort(bank)
    for rect, y in zip(bar, bank):
        rect.set_height(y)
    ax.set_ylim(0,max(bank))
    ax.set_title(i)
    return bar

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1500, interval=1, blit=False)
plt.show()
{% endhighlight %}






[1]:http://www.decisionsciencenews.com/2017/06/19/counterintuitive-problem-everyone-room-keeps-giving-dollars-random-others-youll-never-guess-happens-next/
[2]:https://lucasvw.github.io/main/2017/06/22/money.html
