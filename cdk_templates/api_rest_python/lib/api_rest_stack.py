from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigw,
    aws_iam as iam,
    Duration,
    RemovalPolicy
)
from constructs import Construct

class ApiRestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # --- Configuración de Lambda ---
        # Puedes añadir más configuraciones dinámicamente desde el generador
        lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        # Crea una función Lambda simple que responde a las peticiones
        # En un escenario real, el código de la función Lambda estaría en otra carpeta
        # y se empaquetaría aquí. Para MLP, podemos usar código inline simple.
        lambda_function = lambda_.Function(
            self, "ApiHandlerFunction",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="handler.main", # El archivo se llamará handler.py
            code=lambda_.Code.from_inline("""
import json

def main(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': '¡Hola desde tu API generada por Agentic DevOps Assistant!'})
    }
"""),
            role=lambda_role,
            timeout=Duration.seconds(10),
            memory_size=128
        )

        # --- Configuración de API Gateway ---
        api = apigw.LambdaRestApi(
            self, "ApiGateway",
            handler=lambda_function,
            proxy=True, # Redirige todas las peticiones a la función Lambda
            deploy_options=apigw.StageOptions(
                stage_name="dev", # Nombre del stage (ej. 'dev')
                # logging_level=apigw.MethodLoggingLevel.INFO, # Para habilitar logs de acceso
                # data_trace_enabled=True # Para habilitar data tracing
            ),
            # Restricciones de seguridad básicas, opcional para MLP
            # default_method_options=apigw.MethodOptions(
            #     authorization_type=apigw.AuthorizationType.IAM
            # )
        )

        # Opcional: Añadir tags
        # cdk.Tags.of(self).add("Environment", "dev")
        # cdk.Tags.of(self).add("ManagedBy", "AgenticDevOpsAssistant")

        # Output: URL de la API
        # CfnOutput(self, "ApiEndpoint", value=api.url)