from setuptools import setup, version


setup(name='Inventario',version='1.0.0',packages=['inventario'],
entry_points={
    'console_scripts': ['inventario = inventario.__main__:main']
})