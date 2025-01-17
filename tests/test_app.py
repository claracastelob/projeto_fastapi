from http import (
    # Importando a biblioteca http para testar os códigos de retorno
    HTTPStatus,
)


# Criação da função que testará o código
def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # Act (ação) | O client faz uma requisição chamando o root(/) usando get
    # e guarda em response
    response = client.get('/')

    # assert | Validação da resposta, para ver se retorna 200 (OK)
    assert response.status_code == HTTPStatus.OK
    # asset | Verifica se o retorno de app é igual a esse objeto descrito
    assert response.json() == {'message': 'Olá Mundo!'}


# def test_update_user_should_return_not_found(client):
#     response = client.put(
#         '/users/280',
#         json={
#             'username': 'test',
#             'email': 'test@emailtest.com',
#             'password': 'pass-code-test',
#         },
#     )

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}


# def test_delete_user_should_return_not_found(client):
#     response = client.delete('/users/280')

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}
