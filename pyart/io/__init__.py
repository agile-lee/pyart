"""
Functions to read and write radar and grid data to and from a number of file
formats.

In most cases the :py:func:`pyart.io.read` function should be used to read
in radar data from a file. In certain cases the function the read function
for the format in question should be used.

"""

from .rsl import read_rsl
from .mdv_radar import read_mdv
from .sigmet import read_sigmet
from .chl import read_chl
from .cfradial import read_cfradial, write_cfradial
from .nexrad_archive import read_nexrad_archive
from .nexrad_cdm import read_nexrad_cdm
from .nexradl3_read import read_nexrad_level3
from .uf import read_uf
from .uf_write import write_uf
from .grid_io import read_grid, write_grid
from .output_to_geotiff import write_grid_geotiff
from .auto_read import read
from .mdv_grid import write_grid_mdv, read_grid_mdv
from .common import prepare_for_read
from .arm_sonde import read_arm_sonde_vap, read_arm_sonde

__all__ = [s for s in dir() if not s.startswith('_')]
