from setuptools import setup, find_packages

setup(
    name="maitetsu-voicevox-bridge",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["voicevox-client"],
)
