# The Black Sholes Model: Derivation and Implementation




Central Question: What is the value of an option?


Assumtion


V(s,t) is our option.

s: stochastic process

t:

-> find a trading strategy that replicates the payout of this option.
price of trading stragey = price of option



$\pi = V(s,t) - \triangle S$



$d\pi = dV - \triangle d S$






Ito's Lemma

$dV = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S} + \frac{1}{2}\frac{\partial ^2V}{\partial S^2}dS^2$

$dS$ is given by the geometric brownian motion:

$dS = \mu S d t + \sigma S d W$

$dS^2 =(\mu S d t + \sigma S d W)^2 = \mu^2 S^2 dt^2 + \mu S^2 d t \sigma d W + \sigma^2S^2dW^2$

==>

$dV = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S} + \frac{1}{2}\frac{\partial ^2V}{\partial S^2}(\mu^2 S^2 dt^2 + \mu S^2 d t \sigma d W + \sigma^2S^2dW^2)$

$= \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S} + \frac{1}{2}\frac{\partial ^2V}{\partial S^2}(\mu^2 dt^2 + \mu d t \sigma d W + \sigma^2 dW^2)$


