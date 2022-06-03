import setuptools

setuptools.setup(
    name="myLogger",
    version="1.0",
    license="MIT",
    description="Simple Logger to save info into file",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)