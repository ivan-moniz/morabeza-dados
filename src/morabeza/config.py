"""Leitura da configuração do projeto (Sessão 3)."""
from pathlib import Path

import yaml

CHAVES_OBRIGATORIAS = ("ficheiro_vendas", "moeda")


class ConfigInvalida(Exception):
    """O ficheiro de configuração não existe ou falta-lhe alguma chave obrigatória."""


def carregar_config(caminho: str) -> dict:
    """Lê o ficheiro YAML e devolve um dicionário com a configuração."""
    # TODO 1: se o ficheiro não existir (Path(caminho).exists()), levanta ConfigInvalida.
    # TODO 2: abre o ficheiro com with open(...) e lê-o com yaml.safe_load(ficheiro).
    # TODO 3: vê que chaves de CHAVES_OBRIGATORIAS faltam (compreensão de lista)
    #         e, se faltar alguma, levanta ConfigInvalida com os nomes em falta.
    # TODO 4: devolve o dicionário.
    caminho_path = Path(caminho)
    if not caminho_path.exists():
        raise ConfigInvalida(f"Ficheiro de configuração não existe: {caminho}")
    
    with open(caminho, encoding="utf-8") as ficheiro:
        config = yaml.safe_load(ficheiro)

    chaves_faltantes = [chave for chave in CHAVES_OBRIGATORIAS if chave not in config]
    if chaves_faltantes:
        raise ConfigInvalida(f"Faltam chaves na configuração: {chaves_faltantes}")

    return config


