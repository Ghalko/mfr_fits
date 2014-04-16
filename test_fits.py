import pytest
import mfr_fits
from mfr_fits.render import render_fits_tag
import mock

@pytest.mark.parametrize('filename', [
    'image.fits',
    'image.fit',
    'image.fts',
])
def test_detect_fits_extensions(fakefile, filename):
    fakefile.name = filename
    handler = mfr_fits.Handler()
    assert handler.detect(fakefile) is True

@pytest.mark.parametrize('filename', [
    'image.f',
    'image.it',
    'image.',
    'image.jpg',
    'image.tif',
])
def test_does_not_detect_other_extensions(fakefile, filename):
    fakefile.name = filename
    handler = mfr_fits.Handler()
    assert handler.detect(fakefile) is False

@pytest.mark.parametrize('filename', [
    'image.fits',
    'image.fit',
    'image.fts',
])
def test_replace_extension(filename):
    assert mfr_fits.utils.replace_extension(filename) == 'image.tif'

@pytest.mark.parametrize('filename', [
    '/files/image.fits',
])
def test_dirs_replace_extension(filename):
    assert mfr_fits.utils.replace_extension(filename) == '/files/image.tif'

@pytest.mark.parametrize('filename', [
    'image',
    'image.fi',
])
def test_dont_replace_extension(filename):
    assert mfr_fits.utils.replace_extension(filename) == filename

#@mock.patch('

def test_render_fits_tag(fakefile):
    '''Probably not going to work so well because of dependency '''
    pass
