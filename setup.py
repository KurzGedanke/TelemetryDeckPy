from setuptools import setup

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name='telemetrydeckpy',
    version='1.0.0',
    description='Third party python package to send signals to TelemetryDeck consistently',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Thore D. Jahn',
    author_email='python@kurzgedanke.me',
    url='kurzgedanke.me',
    packages=["telemetrydeckpy"],
    package_data={"": ["LICENSE"]},
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.8",
    license='MIT',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Documentation": "https://github.com/KurzGedanke/TelemetryDeckPy",
        "Source": "https://github.com/KurzGedanke/TelemetryDeckPy",
    },
)
