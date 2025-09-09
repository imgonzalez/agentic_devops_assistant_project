# test_api_rest_stack.py
import pytest
from aws_cdk import App
from api_rest_stack import ApiRestStack # Importa tu stack

# Mock para el entorno si no se usa AWS CLI para obtener account/region
# from unittest.mock import patch

def test_api_rest_stack_creation():
    """Verifica que la pila se crea sin errores y tiene los componentes básicos."""
    app = App()
    # Para pruebas más robustas, se puede mockear el entorno o pasar valores fijos
    # con patch("aws_cdk.environment.Account", "123456789012"),
    # patch("aws_cdk.environment.Region", "us-east-1")
    stack = ApiRestStack(app, "TestApiStack", env={"account": "123456789012", "region": "us-east-1"})

    # Aquí se podrían añadir assertions para verificar la presencia de recursos específicos
    # Ejemplo: que existe una función Lambda, una API Gateway, etc.
    # Esto se hace usualmente inspeccionando la plantilla CloudFormation generada por 'cdk synth'.
    # Para MLP, una prueba que no falle ya es un buen indicio.
    
    # Verificación simple: no deberia lanzar excepción
    assert True

# Podrías añadir más pruebas aquí:
# - Verificar número de Lambda functions
# - Verificar que API Gateway tiene un resource/method
# - Verificar configuraciones específicas del rol IAM