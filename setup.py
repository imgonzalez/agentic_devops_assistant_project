from setuptools import setup, find_packages

setup(
    name='agentic-devops-assistant',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==8.1.7',
        'PyGithub==1.59.0',
        'boto3==1.34.75',
        # 'loguru==0.7.0', # Si se incluye en requirements.txt
    ],
    entry_points={
        'console_scripts': [
            'agentic-devops = agentic_devops.cli:cli',
        ],
    },
    # Puedes añadir aquí metadata adicional: author, description, etc.
)