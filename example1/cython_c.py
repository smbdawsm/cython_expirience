from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("py.module", ["py/module.py"])
]

setup(
    name = 'cython_test',
    cmdclass = {'build_ext': build_ext},
    ext_modules =  ext_modules
)