import sys
from setuptools import find_packages

freeze_cmds = ["bdist_dmg", "bdist_msi", 'build_exe', 'bdist_mac']
if any(x in sys.argv for x in freeze_cmds):
    import glob
    from cx_Freeze import setup, Executable

    executables = [Executable("run_game.py", base=None)]
    build_exe_options = {
        "packages": [
            "pygame"
        ],
        "include_files": glob.glob('assets/original/*'),
    }
    options = {
        "build_exe": build_exe_options,
    }
else:
    executabes = []
    options = {}


setup(
    name='frogger_infinite',
    version='1.0',
    author='David Stuck',
    author_email='david.e.stuck@gmail.com',
    packages=find_packages(),
    package_data={
        'assets': ['assets/original/*'],
    },
    include_package_data=True,
    install_requires=[
        'pygame==1.9.6'
    ],
    executables=executables,
    options=options,
    entry_points={
        'console_scripts': [
            'frogger-infinite=run_game:main',
        ],
    },
)
