from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


class TodoState(str, Enum):
    draft = 'draft'
    todo = 'todo'
    doing = 'doing'
    done = 'done'
    trash = 'trash'


# Faz a conversão de classes python para 'dataclass'
@table_registry.mapped_as_dataclass
class User:
    # Nome da tabela
    __tablename__ = 'users'

    # [mapped_column] Serve para definir propriedades daquela coluna
    # init -> O valor será definido pelo próprio banco de dados
    # primary_key -> informa que esse atributo é a chave primária
    # unique -> esse valor não deve se repetir em outros registros
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    # updated_at: Mapped[datetime] = mapped_column(
    #     init=False,
    #     server_dafault=func.now(),
    #     onupdate=func.now()
    # )


@table_registry.mapped_as_dataclass
class Todo:
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    state: Mapped[TodoState]

    # Toda tarefa pertence a alguém (criando o relacionamento entre tabelas)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
