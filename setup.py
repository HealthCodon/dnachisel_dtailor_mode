import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dnachisel_dtailor_mode", # Replace with your own username
    version="0.1.0",
    author="Li Xing",
    author_email="lix930701@gmail.com",
    description="implement d-tailor method using dnachisel specs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lix1993/dnachisel_dtailor_mode",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)