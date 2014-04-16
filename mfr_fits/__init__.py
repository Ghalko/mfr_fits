# -*- coding: utf-8 -*-
from mfr.core import FileHandler, get_file_extension
from mfr_fits.render import render_fits_tag

__version__ = '0.1.0'
__license__ = 'MIT'
__author__ = 'Bryan Gorges'

try:
    from mfr_fits.export import FitsExporter
    exporter = FitsExporter()
    exporters = {
        'tif': exporter.export_tif,
    }
except ImportError:
    exporters = {}

EXTENSIONS = [
    '.fits',
    '.fit',
    '.fts'
]

class Handler(FileHandler):
    """The fits file handler."""
    renderers = {
        'html': render_fits_tag,
    }

    exporters=exporters

    def detect(self, fp):
        return get_file_extension(fp.name) in EXTENSIONS
