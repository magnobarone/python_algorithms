def ano_bissexto(ano):
    """
    Função que retorna True ou False para o ano Bissexto
    >>> ano_bissexto(2000)
    True
    >>> ano_bissexto(2100)
    False
    >>> ano_bissexto(2400)
    True
    >>> ano_bissexto(3455)
    False
    >>> ano_bissexto(1990)
    False
    >>> ano_bissexto(1992)
    True
    """
    return ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0)
