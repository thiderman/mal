from distutils.core import setup

from mal import __version__

setup(
    name='mal',
    version=__version__.version,
    url='https://github.com/thiderman/mal',
    author='Lowe Thiderman',
    author_email='lowe.thiderman@gmail.com',
    description=('GitHub in your terminal'),
    license='MIT',
    packages=['mal'],
    scripts=[
        'bin/mal'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha'
        'Environment :: Console',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
)
