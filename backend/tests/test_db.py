from sqlalchemy import select

from fast_zero.models import User


# criando o teste, ele usa uma session
def test_create_user(session):
    # Criando um user
    user = User(
        username='clark',
        email='clark@email.com',
        password='minha_senha_legal',
    )

    # Adicionando o registro da sessão, está reservado,
    # mas não foi adicionado ao bd ainda
    session.add(user)
    # Usamos para 'performar' efetivamente as ações no bd
    session.commit()
    """'
    O método scalar() é usado para realizar queries no bd. Ele pega
    o primeiro resultado da busca e faz uma operação de converter o resultado
    do bd em um Objeto criado pelo SQLAlchemy. Nesse caso ele irá converter
    na classe User.
    """
    result = session.scalar(
        select(User).where(User.email == 'clark@email.com')
    )

    assert result.username == 'clark'
