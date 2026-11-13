from setuptools import setup, find_packages

setup(
    name="resmil_core",
    version="0.0.1",
    description="RESMIL Core custom Frappe app",
    author="RESMIL Financial Institution Ltd",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
