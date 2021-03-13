from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cov19',
    packages=find_packages('src'),
    version='0.0.1',
    author_email='momcilo@majic.rs',
    license='GPLv3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/momcilo78/vaccination_news_feed_parser',
    project_urls={
        'Bug Tracker': 'https://github.com/momcilo78/vaccination_news_feed_parser/issue'
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'cov19extract=cob19.main:main',
        ],
    },
)
