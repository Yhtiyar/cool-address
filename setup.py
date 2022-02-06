from setuptools import find_packages, setup



long_description = ""
with open("README.md") as ifp:
    long_description = ifp.read()

setup(
    name="cool-address",
    version="0.0.1",
    packages=find_packages(),
    package_data={"cool-address": ["py.typed"]},
    install_requires=[
        "pysha3<2.0.0,>=1.0.0",
        "web3[tester]",
    ],
    extras_require={
        "dev": [
            "isort",
            "mypy",
            "wheel",
        ],
        "distribute": ["setuptools", "twine", "wheel"],
    },
    description="cool-address: Generate yourself a cool ethereum address/contract address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yhtyyar",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    url="https://github.com/yhtiyar/cool-address/",
    entry_points={"console_scripts": ["cool-address=cool_address.cli:main"]},
    include_package_data=True,
)
