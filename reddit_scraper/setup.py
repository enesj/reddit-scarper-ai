from setuptools import setup, find_packages

setup(
    name='reddit_scraper',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = reddit_scraper.settings']},
    install_requires=[
        'Scrapy',
    ],
)