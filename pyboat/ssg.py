import numpy as np
from numpy import pi

from pyboat.core import ar1_sim

''' Simple functions to create synthetic signal '''

def create_chirp(T1, T2, Nt):

    '''
    Creates a clean chirp signal,
    sweeping linearly through the
    frequencies:

    f_1 = 1/T1, and
    f_2 = 1/T2

    T1: positive float, the period at t = 0, unit is sampling interval
    T2: positive float, the period at t = Nt, unit is sampling interval
    Nt: integer, number of sample points
    '''

    omega_1, omega_2 = 2*pi/T1, 2*pi/T2
    
    tvec = np.arange(Nt)
    
    phases = 0.5/Nt * (omega_2 - omega_1) * tvec**2 + omega_1 * tvec

    return np.cos(phases)

def create_noisy_chirp(T1, T2, Nt, eps, alpha = 0):

    '''
    Creates a clean chirp signal,
    sweeping linearly through the
    frequencies:

    f_1 = 1/T1, and
    f_2 = 1/T2
    
    and adds an AR1 realization
    as background noise.

    Paramters
    ---------
    T1: float, starting period, unit is sampling interval
    T1: float, final period, unit is sampling interval
    Nt: int, number of samples
    eps: float, noise intensity
    alpha: float, AR1 parameter 0 < alpha < 1
    '''

    signal = create_chirp(T1, T2, Nt)
    noise = ar1_sim(alpha = alpha, N = Nt)

    return signal + eps * noise

def create_exp_envelope(tau, Nt):

    '''
    Just returns an exponential
    amplitude envelope with 
    value 1/e after *tau* time elapsed.

    tau: float
    nt: integer, number of sample points
    '''

    tvec = np.arange(Nt)
    env = np.exp(- 1/tau * tvec)

    return env

def assemble_signal(list_of_components, weights):

    '''
    Linearly combines all signal components
    with the given weights.

    list_of_components: list of sequences of same length,
                        the signal components, e.g. chirps, noise, ...
    weights: sequence, 
             the weights (amplitude, noise strengths..) of
             each component
    '''

    if not len(weights) == len(list_of_components):
        raise ValueError('Need as much weights as signal components!')

    cpts = np.array(list_of_components).T # time x component
    cpts = weights * cpts

    signal = np.sum(cpts, axis = 1)
    
    return signal
    
def create_example_trajectory(Nt = 500):

    '''
    Example signal consisting of a chirp
    with exponential envelope and 
    an AR1 background noise
    '''

    s1 = create_chirp(T1 = 20,T2 = 30, Nt = Nt)
    noise = ar1_sim(alpha = 0.3, N = Nt)
    env = create_exp_envelope(tau = Nt*0.7, Nt = Nt)

    signal = assemble_signal([env * s1, noise], [1, 0.5])

    return signal
        
