"""
Módulo normalizador.py
Contiene funciones auxiliares para normalizar texto y facilitar búsquedas.
"""

import unicodedata

def normalizar_texto(texto: str) -> str:
    """
    Normaliza un texto:
        - Lo convierte a minúsculas
        - Elimina acentos

    Args:
        texto (str): Texto a normalizar.

    Returns:
        str: Texto normalizado.
    """
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto