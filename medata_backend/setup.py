import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="medata_backend", 
    version="1.0",
    author="Kevin Kraus, Jan Effenberger, Max Heydemann, Merlin Knäble, Tim Rietz",
    author_email="uvuyo@student.kit.edu",
    description="Backend for Medata",
    url="https://git.scc.kit.edu/issd/students/teamproject/ws20-il/-/tree/master",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)