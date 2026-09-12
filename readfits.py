from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import SimpleNorm



def show_image(filename):
    hdu_list = fits.open(filename)

    header = hdu_list[0].header
    data = hdu_list[0].data

    snorm = SimpleNorm('log', percent=98)

    fig, ax = plt.subplots()
    axim = snorm.imshow(data, ax=ax, origin='lower')
    fig.colorbar(axim, ax=ax)

    plt.show()