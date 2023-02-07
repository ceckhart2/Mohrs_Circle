import math
import numpy as np
import matplotlib.pyplot as plt

class MohrsCircle:
    """Takes Stress Values and calculates various components of those stresses
    as well as plots some of those components and properties
    """

    def __init__(self, sigmax, sigmay, tauxy, units):
        self.sigmax = sigmax
        self.sigmay = sigmay
        self.tauxy = tauxy
        self.units = units

    def sigma_avg(self):
        return round((self.sigmax + self.sigmay) / 2, 2)

    # Returns radius
    def radius(self):
        return round(math.sqrt(((self.sigmax - self.sigmay) / 2) ** 2 + self.tauxy ** 2), 2)

    def taumax(self):
        return self.radius()

    def sigma_1(self):
        return round(self.sigma_avg() + self.radius(), 2)

    def sigma_2(self):
        return round(self.sigma_avg() - self.radius(), 2)

    def angle(self):
        if self.sigmay == self.sigma_avg():
            return 0
        else:
            return math.fabs(round(math.degrees(math.atan(self.tauxy / (self.sigma_avg() - self.sigmay))), 2))

    # Creates plot of data
    def circle_plot(self):
        radians = (np.linspace(0, 360, 361)) * math.pi / 180
        sigma_points = self.sigma_avg() + self.radius() * np.cos(radians)
        tau_points = self.radius() * np.sin(radians)
        plt.figure(figsize=[7, 7])

        # Plots points of relevant data
        plt.plot(sigma_points, tau_points)
        plt.plot([self.sigma_avg(), self.sigmax, self.sigmax, self.sigma_avg()], [0, 0, self.tauxy, 0], 'bo-')
        plt.plot([self.sigma_avg(), self.sigmay, self.sigmay, self.sigma_avg()], [0, 0, -self.tauxy, 0], 'bo-')
        plt.plot(self.sigma_1(), 0, color='r')
        plt.plot(self.sigma_2(), 0)

        # Puts text on important points
        plt.text(self.sigmax, self.tauxy, f'{self.sigmax}, {self.tauxy}', verticalalignment='top', color='r',
                 weight=1000)
        plt.text(self.sigmay, -self.tauxy, f'{self.sigmay}, {-self.tauxy}', verticalalignment='top', color='r',
                 weight=1000)
        plt.text(self.sigma_avg(), 0, self.sigma_avg(), weight=1000, color='r')

        # Misc. chart edits
        plt.grid()
        plt.title("Mohr's Circle")
        plt.xlabel(f'σ ({self.units})')
        plt.ylabel(f'τ ({self.units})')
        plt.gca().invert_yaxis()
        plt.legend(
            [f'Taumax: {self.taumax()}\nSigma1: {self.sigma_1()}\nSigma2: {self.sigma_2()}\nAngle:{self.angle()}'],
            bbox_to_anchor=(0.68, 1.155), loc='upper left', ncol=1, fontsize=6, prop=dict(weight='bold'))

        plt.show()


# Defines User Inuts
sigmax = float(input('Enter Sigma X: '))
sigmay = float(input('Enter Sigma Y: '))
tauxy = float(input('Enter TauXY: '))
units = input('Enter unit type: ')

print('Plotting...')

if __name__ == '__main__':
    mohr1 = MohrsCircle(sigmax, sigmay, tauxy, units)
    mohr1.circle_plot()
