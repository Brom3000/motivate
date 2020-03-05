from setuptools import setup, find_packages

setup(
    name='motivate',
    version='0.2',
    description='A simple script to print random motivational quotes.',
    url='https://github.com/Brom3000/motivate',
    download_url='https://github.com/Brom300/motivate/archive/0.2.tar.gz',
    include_package_data=True,
    author='mubaris',
    author_email='mubarishassannk@gmail.com',
    license='MIT',
    keywords = ['motivation', 'quotes'],
    packages=find_packages(),
    zip_safe=False,
    scripts=['bin/motivate']
    )
