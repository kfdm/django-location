from setuptools import find_packages, setup
from position import __version__

setup(
    name='django-position',
    version=__version__,
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    license='MIT License',
    description='A simple position tracker',
    url='https://github.com/kfdm/django-position',
    author='Paul Traylor',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'djangorestframework',
        'djangorestframework-word-filter',
        'icalendar',
        'pytz',
        'requests',
    ],
    entry_points={
        'django.apps': ['location = position'],
        'django.urls': ['location = position.urls'],
        'rest.apps': ['location = position.views:LocationViewSet'],
    },
)
