import os
import sys

def get_asset_file(asset_file, asset_set='original'):
    if getattr(sys, 'frozen', False):
        asset_path = os.path.join(os.path.dirname(sys.executable), asset_file)
    else:
        asset_path = os.path.abspath('{}/../assets/{}/{}'.format(
            os.path.dirname(os.path.realpath(__file__)),
            asset_set,
            asset_file,
        ))
    return asset_path
