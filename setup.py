from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.carouselbehaviour',
      version=version,
      description="Collective carousel behaviour",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='collective carousel behaviour',
      author='Bogdan Girman',
      author_email='bogdan.girman@gmail.com',
      url='https://github.com/collective/collective.carouselbehaviour',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'plone.namedfile [blobs]',
          'collective.carousel',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      #setup_requires=["PasteScript"],
      #paster_plugins = ["ZopeSkel"],

      )
