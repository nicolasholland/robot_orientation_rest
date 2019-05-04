from os.path import join
import numpy as np
import imageio
from skimage.transform import resize
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import pickle

def resize_dec(func, x=320, y=180):
    def retval(img, *args, **kwargs):
        img_r = resize(img, (y, x), anti_aliasing=True)
        return func(img_r, *args, **kwargs)
    return retval

@resize_dec
def cluster_image(img, n_clusters=10):
    """
    Computes kmeans of an image.

    Parameters
    ----------
    img : np.array

    Returns
    -------
    cluster : tuple, cluster centers
    """
    arr = np.array(img, dtype=np.float64) / 255

    w, h, d = tuple(arr.shape)
    image_array = np.reshape(arr, (w * h, d))
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(image_array)

    return kmeans.cluster_centers_.reshape((3 * n_clusters))


def train():
    model = LinearRegression()

    # labels
    orientations = ['north', 'east', 'south', 'west']
    lb = preprocessing.LabelBinarizer()
    lb.fit(orientations)
    y = lb.transform(orientations)

    # data
    north = imageio.imread(join('images', 'north.png'))[:, :, :3]
    east = imageio.imread(join('images', 'east.png'))[:, :, :3]
    west = imageio.imread(join('images', 'west.png'))[:, :, :3]
    south = imageio.imread(join('images', 'south.png'))[:, :, :3]
    x = np.array([cluster_image(ori) for ori in [north, east, south, west]])

    # training
    model.fit(x, y)
    pickle.dump(model, open('model.pkl', 'wb'))

if __name__ == '__main__':
    train()
