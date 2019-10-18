import large_image
import os
import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline

wsi_path = '/home/sai/Documents/ML/PROJECTS/GLIOMA/DATA/gdc_download_20190927_061123.551856/faa7997c-1979-46ab-9450-92dc62870a24/TCGA-DU-5847-01Z-00-DX1.b7d7de58-38b6-4686-8588-a2542c8595b4.svs'

ts = large_image.getTileSource(wsi_path)

print("Metadata : \n", ts.getMetadata())
print("NativeMagnification : \n", ts.getNativeMagnification())

# num_tiles = 0

# tile_means = []
# tile_areas = []

# for tile_info in ts.tileIterator(
#     region=dict(left=5000, top=5000, width=20000, height=20000, units='base_pixels'),
#     scale=dict(magnification=20),
#     tile_size=dict(width=1000, height=1000),
#     tile_overlap=dict(x=50, y=50),
#     format=large_image.tilesource.TILE_FORMAT_PIL
# ):

#     if num_tiles == 100:
#         print('Tile-{} = '.format(num_tiles))
#         display(tile_info)

#     im_tile = np.array(tile_info['tile'])
#     tile_mean_rgb = np.mean(im_tile[:, :, :3], axis=(0, 1))

#     tile_means.append( tile_mean_rgb )
#     tile_areas.append( tile_info['width'] * tile_info['height'] )

#     num_tiles += 1

# slide_mean_rgb = np.average(tile_means, axis=0, weights=tile_areas)

# print('Number of tiles = {}'.format(num_tiles))
# print('Slide mean color = {}'.format(slide_mean_rgb))

pos = 800

tile_info = ts.getSingleTile(
    tile_size=dict(width=1000, height=1000),
    scale=dict(magnification=30),
    tile_position=pos
)

plt.imshow(tile_info['tile'])
plt.show()