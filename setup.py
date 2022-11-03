from setuptools import setup, find_packages


setup(
    name='tular',
    version='0.0',
    description='tular',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clld>=9.2.2',
        'conllu',
        'zenodoclient>=0.4',
        'clld-glottologfamily-plugin>=4.0',
        'clld-cognacy-plugin',
        'clld-ipachart-plugin>=0.2',
        'pyglottolog',
        'clldmpg>=4.2',
        'pyclts>=3.0',
],
extras_require={
        'dev': ['flake8', 'waitress'],
        'test': [
            'pytest>=5.4',
            'pytest-clld',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
            'selenium',
            'zope.component>=3.11.0',
        ],
    },
    test_suite="tular",
    entry_points="""\
    [paste.app_factory]
    main = tular:main
""")
