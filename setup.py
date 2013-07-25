from setuptools import setup, find_packages

setup(
    name='Wunderground',
    version='0.0.1',
    description='Django Weather Underground',
    long_description=(open('README.rst', 'r').read() +
                      open('AUTHORS.rst', 'r').read() +
                      open('CHANGELOG.rst', 'r').read()),
    author='SI-Works',
    author_email='developers@siworks.co.za',
    license='BSD',
    url='http://github.com/ratt/django-wunderground',
    packages = find_packages(),
    install_requires = [
        'south',
        'urllib2'
    ],
    include_package_data=True,
    tests_require=[
        'django-setuptest',
        'coverage',
    ],
    test_suite="setuptest.SetupTestSuite",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)