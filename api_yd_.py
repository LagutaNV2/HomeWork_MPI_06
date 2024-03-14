import requests


class Test_YD_Create_Folder:
    def setup_method(self):
        self.headers = {
            'Authorization': '______________'
        }

    def teardown_method(self):
        params = {
            'path': 'Folder_1'
        }
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        
    def test_create_folder(self):
        params = {
            'path': 'Folder_1'
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        assert response.status_code == 201

    def test_create_folder_409(self):
        params = {
            'path': 'Folder_2'
        }
        requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                     params=params,
                     headers=self.headers)
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        assert response.status_code == 409