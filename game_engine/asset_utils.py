import os

def get_asset_file(asset_file, asset_set='draft'):
    asset_path = os.path.abspath('{}/../assets/{}/{}'.format(
        os.path.dirname(os.path.realpath(__file__)),
        asset_set,
        asset_file,
    ))
    return asset_path
