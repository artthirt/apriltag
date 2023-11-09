from distutils.core import setup, Extension
import numpy as np
import sys
import os

sources = [
    'apriltag_pywrap.c',
    'apriltag.c',
    'apriltag_pose.c',
    'apriltag_quad_thresh.c',
    'tag16h5.c',
    'tag25h9.c',
    'tag36h10.c',
    'tag36h11.c',
    'tagCircle21h7.c',
    'tagCircle49h12.c',
    'tagCustom48h12.c',
    'tagStandard41h12.c',
    'tagStandard52h13.c',
    'common/workerpool.c',
    'common/g2d.c',
    'common/getopt.c',
    'common/homography.c',
    'common/image_u8.c',
    'common/image_u8x3.c',
    'common/image_u8x4.c',
    'common/matd.c',
    'common/pam.c',
    'common/pjpeg-idct.c',
    'common/pjpeg.c',
    'common/pnm.c',
    'common/svd22.c',
    'common/string_util.c',
    'common/time_util.c',
    'common/unionfind.c',
    'common/zarray.c',
    'common/zhash.c',
    'common/zmaxheap.c',
    'common/pthreads_cross.cpp'
]

include_dirs = [
    '.',
    np.get_include()
]

library_dirs = []

libraries = []

def generate_include_text(infile, outfile):
    with open(infile, 'r') as fi, open(outfile, 'w') as fo:
        txt = fi.read()
        txt = txt.replace('"', '\\"').replace('\n', '\\n')
        txt = f'("{txt}")'
        fo.write(txt)

generated = [
    'apriltag_detect.docstring',
    'apriltag_py_type.docstring',
]

for x in generated:
    xh = f'{x}.h'
    os.remove(xh)
    generate_include_text(x, xh)

module = Extension("apriltag",
                   sources=sources,
                   include_dirs=include_dirs,
                   library_dirs=library_dirs,
                   libraries=libraries)

setup(name = 'apriltag_python',
      version='1.0',
      description='April Tag',
      data_files=[],
      install_requires=["numpy"],
      ext_modules=[module])