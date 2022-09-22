from setuptools import setup, find_packages
 
setup(
    name="xray-test",
    version="0.1",
    description="Simple hello-world application to test xray integration in the build process",
    author="Mictest",
    author_email="ben.roberts@example.com",
    url="https://example.com/xray-test",
    packages=find_packages(exclude=['tests*']),
    install_requires=['PyYAML'],
)
