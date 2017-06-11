from setuptools import setup, Extension
# from distutils.extension import Extension
from Cython.Build import cythonize
# import os.path as osp

setup(
    ext_modules=cythonize([
        Extension("winpty", sources=["winpty/winpty.pyx"],
                  libraries=["winpty"],
                  extra_compile_args=["-Zi", "/Od"],
                  extra_link_args=["-debug"])
    ]),
)
