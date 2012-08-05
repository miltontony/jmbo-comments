from setuptools import setup, find_packages

def listify(filename):
    return filter(None, open(filename,'r').read().split('\n'))

setup(
    name = "jmbo-comments",
    version = "0.0.2",
    url = 'http://github.com/praekelt/jmbo-comments',
    license = 'BSD',
    description = 'Comments module based on jmbo-comments',
    author = 'Praekelt Foundation',
    author_email = 'dev@praekeltfoundation.org',
    packages = find_packages(),
    install_requires = [
        'setuptools',
        'django-nose',
        'django-category',
        'django-dirtyfields',
        'South==0.7.3',
        'django_ckeditor-dev',
    ],
    dependency_links = [
        'https://github.com/dwaiter/django-ckeditor/tarball/master#egg=django_ckeditor-dev',
    ],
    classifiers = [
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking'
    ]
)
