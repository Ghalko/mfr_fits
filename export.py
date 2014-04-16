# -*- coding: utf-8 -*-
"""Fits exporter module."""
import subprocess as sub
import os
import utils

class FitsExporter(object):

    def export_tif(self, fp):
        return utils.convert_fits_to_tif(fp, config['SAVE_PATH'],
                                         config['SAVE_PATH'])
