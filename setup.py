from distutils.core import setup

import sys

if sys.version_info >= (3, 2):
    install_requires = []
else:
    install_requires = ["functools32"]

setup(
    name="geomag",
    packages=["geomag"],
    # data_files = [('geomag', ('geomag/WMM.COF',))],
    package_data={"geomag": ["model_data/*.COF"]},
    include_package_data=True,
    version="0.9.2015",
    description="Magnetic variation/declination",
    author="Christopher Weiss",
    author_email="cmweiss@gmail.com",
    url="http://geomag.googlecode.com/",
    download_url="//pypi.python.org/packages/source/g/geomag/geomag-0.9.2015.zip",
    keywords=["magnetic", "variation", "declination"],
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Utilities",
    ],
    long_description="""\
Magnetic variation/declination
------------------------------

Calculates magnetic variation/declination for any latitude/longitude/altitude,
for any date. Uses the NOAA National Geophysical Data Center, epoch 2015 data.
""",
)
