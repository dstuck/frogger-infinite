from frogger_infinite import GridStruct


def get_grid_center(x, y, grid_size=GridStruct.GRID_SIZE):
    return (
        x * grid_size + grid_size / 2 + GridStruct.GRID_OFFSET_X,
        y * grid_size + grid_size / 2 + GridStruct.GRID_OFFSET_Y,
    )


def get_grid_corner(x, y, grid_size=GridStruct.GRID_SIZE):
    return (
        x * grid_size + GridStruct.GRID_OFFSET_X,
        y * grid_size + GridStruct.GRID_OFFSET_Y,
    )
