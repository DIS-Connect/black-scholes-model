import numpy as np
from scipy.stats import norm
import datetime as dt
from datetime import datetime



def option_price(r, S, K, T, sigma, type):

    d1 = (np.log(S/K) + (r+ sigma**2/2)*T)/(sigma*np.sqrt(T))

    d2 = d1 - sigma*np.sqrt(T)

    if type == "CALL":
        price = S*norm.cdf(d1,0,1) - K*np.exp(-r*T)*norm.cdf(d2,0,1)
    elif type == "PUT":
        price = K*np.exp(-r*T)*norm.cdf(-d2,0,1) - S*norm.cdf(-d1, 0, 1)

    return price




def delta(r, S, K, T, sigma, type):

    d1 = (np.log(S/K) + (r+ sigma**2/2)*T)/(sigma*np.sqrt(T))

    if type == "CALL":
        price = norm.cdf(d1,0,1)
    elif type == "PUT":
        price = -norm.cdf(-d1,0,1)

    return price



def gamma(r, S, K, T, sigma, type):

    d1 = (np.log(S/K) + (r+ sigma**2/2)*T)/(sigma*np.sqrt(T))

    if type == "CALL":
        return norm.pdf(d1,0,1)/(S * sigma * np.sqrt(T))
    elif type == "PUT":
        return norm.pdf(d1,0,1)/(S * sigma * np.sqrt(T))



def vega(r, S, K, T, sigma, type):

    d1 = (np.log(S/K) + (r+ sigma**2/2)*T)/(sigma*np.sqrt(T))

    if type == "CALL" or type == "PUT":
        return 0.01 * S * norm.pdf(d1,0,1) * np.sqrt(T)


def theta(r, S, K, T, sigma, type):

    d1 = (np.log(S/K) + (r+ sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    if type == "CALL":
        return ((-S*norm.pdf(d1,0,1)*sigma)/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2) )/365
    elif type == "PUT":
        return ((-S*norm.pdf(d1,0,1)*sigma)/(2*np.sqrt(T)) + r*K*np.exp(-r*T)*norm.cdf(-d2) )/365


def rho(r, S, K, T, sigma, type):

    d1 = (np.log(S/K) + (r+ sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    if type == "CALL":
        return 0.01*K*T*np.exp(-r*T)*norm.cdf(d2)
    elif type == "PUT":
        return 0.01*-K*T*np.exp(-r*T)*norm.cdf(-d2)