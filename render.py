"""FITS renderer module"""
import os
from mfr_fits import utils
from mfr_fits.configuration import config

def render_fits_tag(fp, src=None, alt='', **kwargs):
    """A fits renderer, might be replaced
    by image renderer because output is an image

    """
    #use filepointer for filename
    if src is None:
        src = fp.name
    tif_src = utils.replace_extension(src)
    utils.convert_fits_to_tif(fp, inpath=config['IN_PATH'],
                              outpath=config['OUT_PATH'])
    return '<img src="{src}" alt="{alt}"/>'.format(src=tif_src, alt=alt)
