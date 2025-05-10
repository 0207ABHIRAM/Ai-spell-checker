from setuptools import setup, find_packages

setup(
    name='spell-checker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'scikit-learn',
        'torch',
        'transformers'
    ],
    author='Your Name',
    description='An AI-based spell checker.',
    license='MIT'
)
