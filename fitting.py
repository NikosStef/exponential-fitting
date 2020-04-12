import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-x/b) + c

def main():

    url = "/root/Downloads/90_modified.csv"
    df = pd.read_csv(url, header=None)
    df.columns = ['x', 'y']
    #df.sort_values(by=['x'])

    x = df['x']
    y = df['y']

    """
    x1 = df['x'].loc[df['x'] <= 0.0005]
    x2 = df['x'].loc[df['x'] > 0.0005]
    y1 = df['y'].loc[df['x'] <= 0.0005]
    y2 = df['y'].loc[df['x'] > 0.0005]
    """

    #poly_fit = np.poly1d(np.polyfit(x,y,3))

    popt, pcov = curve_fit(func, x, y, method="trf")


    #popt1, pcov1 = curve_fit(func, x1, y1, method="trf")
    #popt2, pcov2 = curve_fit(func, x2, y2, method="trf")

    plt.figure()
    plt.plot(x, y, 'ko', label="Original Noised Data")
    #plt.plot(x, poly_fit(x), 'r-', label="Fitted Curve")
    plt.plot(x, func(x, *popt), 'r-', label="Fitted Curve")
    #plt.plot(x1, func(x1, *popt1), 'r-', label="Fitted Curve")
    #plt.plot(x2, func(x2, *popt2), 'g-', label="Fitted Curve")

    plt.legend()
    plt.savefig("plot_mod.png")
    plt.show()

    with open("coef_mod.txt", "w") as file:
        file.write("Modified Data:\n\n")
        for i, v in enumerate(['a','b','c']):
            file.write("{}: {}".format(v, popt[i]))
            file.write("\n")

        file.write(f"\nFunction: {popt[0]} * e^(-x/{popt[1]}) + {popt[2]}")

if __name__=="__main__":
    main()
