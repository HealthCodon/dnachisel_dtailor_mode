import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

projectname = "dnachisel_dtailor_mode"
exec(open('%s/version.py' % projectname).read())  # loads __version__
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=projectname,
    version=__version__,
    author='Li Xing',
    author_email="lix930701@gmail.com",
    description="implement d-tailor method using dnachisel specs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lix1993/dnachisel_dtailor_mode",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
