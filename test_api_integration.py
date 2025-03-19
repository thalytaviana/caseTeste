import unittest
import requests

class TestAPIIntegration(unittest.TestCase):
    BASE_URL = "http://localhost:3000"  
    ROUTE = "/api/v1/institutions/"  ##colocar aqui a rota para a requisição da api
    TOKEN = "g3-d72f4d0e90fce94208a9cc383c7e10ae7b"  
    

    def test_api_data_fetch(self):
        headers = {
            "Authorization": f"Bearer {self.TOKEN}"
        }

        url = self.BASE_URL + self.ROUTE
        print(f"Testando requisição para: {url}")
        
        response = requests.get(url, headers=headers)

        self.assertEqual(response.status_code, 200, f"Erro: Status retornado foi {response.status_code}, esperado 200.")


        try:
            data = response.json()
        except Exception as e:
            self.fail(f"Erro ao converter resposta para JSON: {e}")
        
        self.assertIsInstance(data, list, "Os dados retornados não são uma lista.")
        self.assertGreater(len(data), 0, "Nenhum dado foi retornado pela API.")

        print("Teste concluído com sucesso! Dados retornados:")
        print(data)

if __name__ == '__main__':
    unittest.main()
