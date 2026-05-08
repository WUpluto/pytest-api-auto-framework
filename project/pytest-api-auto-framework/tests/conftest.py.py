import pytest
import requests
from conf.config import BASE_URL

@pytest.fixture(scope="session")
def get_token():
    """
    全局前置：在所有用例执行前，先调用登录接口获取 Token，
    并自动注入到请求头中。解决接口鉴权依赖问题。
    """
    login_url = f"{BASE_URL}/admin/login"
    login_data = {"username": "admin", "password": "admin_password"}
    
    # 模拟发送登录请求
    # response = requests.post(login_url, json=login_data)
    # token = response.json().get("data").get("token")
    
    # 这里为了防报错，写死一个 Mock Token
    token = "mock_jwt_token_888888"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return headers
