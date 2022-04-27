def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1>Page d'acceuil général</h1>".encode() in response.data