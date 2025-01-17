from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Objeto pydantic-settings que carrega as variáveis
    # em um arquivo de configuração
    model_config = SettingsConfigDict(
        # Definimos o caminho para o arquivo de configuração e seu encoding
        env_file='.env',
        env_file_encoding='utf-8',
    )
    # Essa variável será preenchida com o valor encontrado
    # com o mesmo nome no arquivo .env
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


# O arquivo .env é o ambiente de configuração do código, ele é oculto.
# Eu criei um novo arquivo chamado .env na raiz desse projeto
# e adicionei essa variável lá
