from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Planning',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10 :: Linux :: Mac',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='LogsTf',
  version='0.0.0',
  description='Wrapper around the Logs.tf website',
  long_description="",
  url='',  
  author='Lucas Cerqueira',
  author_email='lucascerqueirabank@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['tf2', 'logstf', 'webscraping'], 
  packages=find_packages(),
  install_requires=['lxml', 'requests', 'beautifulsoup4'] 
)