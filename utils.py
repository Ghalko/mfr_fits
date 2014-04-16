import subprocess as sub
import os
import mfr.core

def convert_fits_to_tif(fp, inpath, outpath):
    filename = fp.name
    savename = filename.split('.')[0] + '.tif'
    fullin = os.path.join(inpath,filename)
    fullout = os.path.join(outpath,savename)
    stiff = " ".join(["stiff", fullin, "-OUTFILE_NAME", fullout,
                      "-WRITE_XML", "N", "-VERBOSE_TYPE", "QUIET"])
    process = sub.call(stiff, shell=True)
    print process
    return fullout

def replace_extension(filepath, old=('fits','fit','fts'),
                      new='tif'):
    filesplit = filepath.split('.')
    oldext = mfr.core.get_file_extension(filepath).lstrip('.')
    #returns if no file extensions
    if len(filesplit) == 1:
        return filepath
    #Checks for single string as old extension
    if isinstance(old, basestring):
        if old == oldext:
            return filesplit[0] + '.' + new
        return filepath
    #Checks for extension in tuple or list
    if oldext in old:
        return filesplit[0] + '.' + new
    return filepath
