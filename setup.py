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
    install_requires = [
        'rea-serializers',
        'django-denormalize',
        'pymongo',
    ],
    dependency_links = [
        'git+git@github.com:commoncode/rea-serializers.git#egg=rea-serializers',
    ]
)
