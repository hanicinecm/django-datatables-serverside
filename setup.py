from distutils.core import setup

setup(
    name='django_datatables_serverside',
    description='A basic yet highly customizable Django app for integration of DataTables.net '
                'into Django 3 projects in the server-side mode.',
    version='0.0',
    author='Martin Hanicinec',
    author_email='hanicinecm@gmail.com',
    packages=['django_datatables_serverside'],
    install_requires=['Django>=2.0']
)
