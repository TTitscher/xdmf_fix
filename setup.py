import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xdmf_fix",
    version="0.4",
    author="Thomas Titscher",
    author_email="thomas.titscher@gmail.com",
    description="A tiny package to modify the node order of quadratic triangles and tets in a gmsh .msh to work with FEniCS/DOLFIN.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TTitscher/xdmf_fix",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["xdmf-fix = xdmf_fix.xdmf_fix:cli"]}
)
