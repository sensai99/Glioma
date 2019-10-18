import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import large_image
from PIL import Image
wsi_path = 'slide.svs'
# %matplotlib inline

# wsi_url = 'https://data.kitware.com/api/v1/file/5899dd6d8d777f07219fcb23/download'

# wsi_path = 'TCGA-02-0010-01Z-00-DX4.07de2e55-a8fe-40ee-9e98-bcb78050b9f7.svs'
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
ts = large_image.getTileSource(wsi_path)
num_tiles = 0
# print(wsi_path)
tile_means = []
tile_areas = []
it=0
for tile_info in ts.tileIterator(
    region=dict(left=5000, top=5000, width=20000, height=20000, units='base_pixels'),
    scale=dict(magnification=20),
    tile_size=dict(width=1000, height=1000),
    tile_overlap=dict(x=50, y=50),
    format=large_image.tilesource.TILE_FORMAT_PIL
):
    it+=1
    im_tile = (tile_info['tile'])
    print(it, tile_info['gheight'],tile_info['gheight'])
    plt.imshow(im_tile)
    # plt.show()
    if tile_info['gwidth']==2000 and tile_info['gheight']==2000:
        im_tile.convert('LA').save(str("im1/grayscale/")+str(it)+'.png')
        plt.savefig(str("im1/color/")+str(it)+'.png')
    # tile_mean_rgb = np.mean(im_tile[:, :, :3], axis=(0, 1))

    # tile_means.append( tile_mean_rgb )
    tile_areas.append( tile_info['width'] * tile_info['height'] )

    num_tiles += 1

# slide_mean_rgb = np.average(tile_means, axis=0, weights=tile_areas)
# print(it)
print('Number of tiles = {}'.format(num_tiles))
# print('Slide mean color = {}'.format(slide_mean_rgb))
ts.getNativeMagnification()
ts.getMagnificationForLevel(level=0)