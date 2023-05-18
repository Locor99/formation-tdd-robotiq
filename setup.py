from setuptools import setup, find_packages

setup(name='AxcetaFormationPython',
      version='0.0.1',
      description='Axceta Solutions inc. Formation Python',
      url='https://gitlab.com/axceta/axceta/box/iiot-thing',
      author='Thierry Mailloux',
      author_email='olivier.dugas.1@gmail.com',
      packages=find_packages(exclude=["tests"]),
      zip_safe=False,
      include_package_data=True,
      install_requires=[
      ],
      extras_require={},
      test_suite='nose.collector',
      tests_require=['nose']
      )
