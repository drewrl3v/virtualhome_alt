import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements.txt file and convert to a list
with open("./virtualhome/requirements.txt", "r", encoding="utf-8") as f:
    install_requires = f.read().splitlines()

# This is an alternative repo to the standard virtualhome repo created by Xavier Puig
setuptools.setup(
    name="virtualhome",
    version="0.0.1",
    author="Andrew Lizarraga", # Original Author: Xavier Puig
    author_email="drewrl3v@gmail.com",
    description="Python API to communicate with the VirtualHome environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drewrl3v/virtualhome_alt",
    #project_urls={
    #    "Documentation": "http://virtual-home.org/docs/",
    #    "Bug Tracker": "https://github.com/xavierpuigf/virtualhome/issues"
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Found in the requirements.txt
    install_requires = install_requires,
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.10",
)