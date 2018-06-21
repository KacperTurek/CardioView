import wfdb
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def load_signal(database_id, signal_number):
    database = '{}/'.format(database_id)
    signal = signal_number
    record = wfdb.rdrecord(signal, pb_dir=database)
    annotation = wfdb.rdann(signal, 'atr', pb_dir=database)
    return(record.p_signal, record.comments, record.__dict__, annotation)

def plot_signal(signal_array, annotation):
    fig, ax = plt.subplots()
    t = np.linspace(0, int((len(signal_array))/360), int(len(signal_array)))
    ax.plot(t, signal_array[:, 1])
    # ax.scatter(t, annotation, c='red')
    l = type(annotation)
    ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='ECG plot')
    ax.grid()
    plt.show()
    return(l)
