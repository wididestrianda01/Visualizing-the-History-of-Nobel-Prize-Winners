from setuptools import setup, find_packages

setup(
    name="template-project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pandas", "numpy", "scikit-learn", "jupyter"],
    entry_points={
        "console_scripts": [
            "template-script=template_project.cli:main",
        ],
    },
)
