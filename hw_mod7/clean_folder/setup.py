from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Allows to sort several file types to appropriate folders',
    url='https://github.com/Pavlomatolikov/hw_mod6/blob/master/mod6.py',
    author='Pavlo',
    author_email='pavlo@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean = clean_folder.clean:main']},
)
