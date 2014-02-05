from setuptools import setup, find_packages

setup( name='rea-collections',
    version = '0.0.1',
    description = 'Collections (mongo) for REA',
    author = 'Daryl Antony',
    author_email = 'daryl@commoncode.com.au',
    url = 'https://github.com/commoncode/rea-collections',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    dependency_links = [
        'http://github.com/commoncode/entropy/tarball/master#egg=django-entropy',
        'http://github.com/commoncode/rea-serializers/tarball/master#egg=rea-serializers',
    ],
    setup_requires = [
        'pip',
    ],
    install_requires = [
        'rea-serializers',  # which in turn requires `rea`
        'django-denormalize',
        'pymongo',
    ],
)
