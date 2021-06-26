from distutils.core import setup

setup(
    name="ps_tap_jira",  # How you named your package folder (MyLib)
    packages=["ps_tap_jira"],  # Chose the same as "name"
    version="3.0",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="tap_jira package for ps",  # Give a short description about your library
    author="Sai Anil",  # Type in your name
    author_email="cannot.give@myemail.tou",  # Type in your E-Mail
    url="https://github.com/saianil58/ps_tap_jira",  # Provide either the link to your github or to your website
    download_url="https://github.com/saianil58/ps_tap_jira/archive/refs/tags/3.0.tar.gz",  # I explain this later on
    keywords=[
        "tap_jira",
    ],  # Keywords that define your package best
    py_modules=["tap_jira"],
    install_requires=[
        "singer-python==5.4.1",
        "requests==2.20.0",
    ],
    extras_require={"dev": ["pylint", "nose", "ipdb"]},
    entry_points="""
          [console_scripts]
          tap-jira=tap_jira:main
      """,
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.6",
    ],
    package_data={"schemas": ["tap_jira/schemas/*.json"]},
    include_package_data=True,
)
