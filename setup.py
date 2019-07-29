from setuptools import setup

setup(
    name="autopwn",
    version="0.1",
    url="https://github.com/xentrick/autopwn",
    license="",
    author="nmavis",
    author_email="nmavis@cisco.com",
    description="Python CLI tools for checking vulnerable services in MS3",
    packages=["autopwn", "autopwn.bin", "autopwn.services", "autopwn.util"],
    entry_points={"console_scripts": ["autopwn = autopwn.bin.cli:main"]},
    install_requires=["python-magic", "pymetasploit3"],
)
