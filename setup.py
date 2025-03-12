from setuptools import setup, find_packages

setup(
    name="dof_reality_controller",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "pyserial"
    ],
    entry_points={
        "console_scripts": [
            "dof-reality=dof_reality.main:main"
        ]
    },
)
