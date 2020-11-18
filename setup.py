from setuptools import setup, find_packages

setup(
    name="usplash-downloader",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "requests"
    ],
    entry_points="""
        [console_scripts]
        usdl=usplash_downloader.main:main
    """,
)
