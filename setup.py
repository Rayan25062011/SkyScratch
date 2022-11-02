from setuptools import setup

setup(name='SkyScratch',
      version='1.2.0',
      description='VPN library that will duisguise you while browsing the web',
      author='Rayan25062011',
      url='https://github.com/Rayan25062011/SkyScratch',
      install_requires=['requests', 'socket', 'subprocess', 'signal', 'sys', 'os'],
      packages=['SkyScratch'],
      package_dir={
          'SkyScratch': 'SkyScratch/skyscratch'
      },
      scripts=['SkyScratch/skyscratch']
      )
