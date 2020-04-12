
# specify classifiers
BIGARTM_CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Software Development'
]

setup_kwargs = dict(
    # some common information
    name='bigartm',
    version='0.9.2',

    # package_dir={'': './python'},

    # information about dependencies
    install_requires=[
        'pandas',
        'numpy',
        'tqdm',
        'protobuf>=3.0'
    ],
    # this option must solve problem with installing
    # numpy as dependency during `setup.py install` execution
    # some explanations here:
    # https://github.com/nengo/nengo/issues/508#issuecomment-64962892
    # https://github.com/numpy/numpy/issues/2434#issuecomment-65252402
    setup_requires=[
        'numpy'
    ],

    # metadata for upload to PyPI
    license='New BSD license',
    url='https://github.com/bigartm/bigartm',
    description='BigARTM: the state-of-the-art platform for topic modeling',
    classifiers=BIGARTM_CLASSIFIERS,
    # Who should referred as author and how?
    # author = 'Somebody'
    # author_email = 'Somebody\'s email'
    # Now include `artm_dev` Google group as primary maintainer
    maintainer='ARTM developers group',
    maintainer_email='artm_dev+pypi_develop@googlegroups.com'
)


