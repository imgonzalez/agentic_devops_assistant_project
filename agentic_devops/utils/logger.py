import logging

def setup_logging(name: str, level=logging.INFO):
    """Configura un logger básico."""
    logger = logging.getLogger(name)
    if not logger.handlers: # Evitar añadir handlers múltiples si ya existe
        logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        logger.propagate = False # Evitar que se propague al root logger
    return logger

# logger = setup_logging(__name__) # Ejemplo de uso