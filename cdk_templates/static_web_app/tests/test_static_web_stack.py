import pytest
from aws_cdk import App
from lib.static_web_stack import StaticWebStack

def test_static_web_stack_creation():
    app = App()
    stack = StaticWebStack(app, "TestStaticWebStack", env={"account": "123456789012", "region": "us-east-1"})
    assert True
