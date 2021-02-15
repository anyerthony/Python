from setuptools import setup, version


setup(name='Proyecto',version='1.0.0',packages=['Proyecto'],
entry_points={
    'console_scripts': ['Proyecto = Proyecto.__main__:main']
})