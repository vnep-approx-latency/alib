from setuptools import setup, find_packages

install_requires = [
    # "gurobipy",  # install this manually
    "matplotlib",
    "numpy",
    "click",
    "pyyaml",
    "jsonpickle",
    "unidecode",
    "networkx",
    "pytest"
]

setup(
    name="alib",
    python_requires=">=3.7",
    packages=["alib"],
    package_data={"alib": ["data/topologyZoo/*.yml"]},
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "alib = alib.cli:cli",
        ]
    }
)
