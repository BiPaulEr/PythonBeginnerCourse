from setuptools import setup, Extension

module = Extension(
    'monsters',
    sources=['monsters_c_src/monsters.c']
)

setup(
    name='monsters-c',
    version='1.0.0',
    description='Module C pour gérer des monstres',
    ext_modules=[module],
)
