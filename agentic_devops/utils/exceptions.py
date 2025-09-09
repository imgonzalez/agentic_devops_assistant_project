class AgentDevOpsError(Exception):
    """Clase base para errores específicos del Agentic DevOps Assistant."""
    pass

class GitHubAPIError(AgentDevOpsError):
    """Error relacionado con la API de GitHub."""
    pass

class CDKGenerationError(AgentDevOpsError):
    """Error durante la generación de código CDK."""
    pass