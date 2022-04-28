from setuptools import setup, find_packages


REQUIREMENTS_FILE_PATH = 'requirements.txt'


def load_requirements():
    with open(REQUIREMENTS_FILE_PATH) as file:
        return file.read().splitlines()


setup(
    name='moonscan',
    version='0.1.0',
    description='Scan the LAN',
    author='Elai Corem',
    packages=find_packages(include=['moonscan', 'moonscan.*']),
    install_requires=load_requirements(),
    entry_points={
        'console_scripts': ['moonscan=moonscan.__main__:main']
    },
)
