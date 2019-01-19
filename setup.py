import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="investment_calculator",
    version="0.0.1",
    author="Mohammad Mahjoub",
    author_email="youvsyou47@gmail.com",
    description="Real estate investment calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hyped-247/wealth-maneger-CLT.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)