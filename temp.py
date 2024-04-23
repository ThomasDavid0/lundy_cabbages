import numpy as np
import matplotlib.pyplot as plt
img_name = 'DJI_20240423180105_0006_'


img = {b: plt.imread(f'DJI_20240423180105_0006_MS_{b}.TIF') for b in ['G', 'NIR', 'R', 'RE']}

normalizer = np.percentile(img['R'], 95)

r = img['R'] / normalizer
nir = img['NIR'] / normalizer

oar = (nir - r) / (nir + r)

oar[oar < 0.7] = 0

#plt.imshow(oar, interpolation='nearest')
#plt.show()

plt.imsave(f'{img_name}_processed.jpg', oar)
#img_arr = cv2.imread('DJI_20240423180105_0006_D.JPG')

#print(img)