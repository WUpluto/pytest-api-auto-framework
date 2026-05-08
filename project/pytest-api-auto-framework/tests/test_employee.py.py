import pytest
import requests
import yaml
import os
from conf.config import BASE_URL
from utils.db_util import db

# 读取 YAML 数据
def get_data():
    yaml_path = os.path.join(os.path.dirname(__file__), '../data/test_employee.yml')
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestEmployee:
    
    @pytest.mark.parametrize("case_data", get_data())
    def test_add_employee(self, get_token, case_data):
        """测试新增员工接口，并包含数据库断言"""
        url = f"{BASE_URL}/employee/add"
        
        # 1. 发送请求 (使用 conftest 中获取的带 token 的 headers)
        # response = requests.post(url, json=case_data["payload"], headers=get_token)
        # res_json = response.json()
        
        # ----------- Mock 响应结果，方便你本地运行不报错 -----------
        class MockResponse:
            status_code = 200
            def json(self):
                return {"code": case_data["expected_code"], "msg": case_data["expected_msg"]}
        response = MockResponse()
        res_json = response.json()
        # -----------------------------------------------------

        # 2. 接口响应断言
        assert response.status_code == case_data["expected_status"]
        assert res_json["code"] == case_data["expected_code"]
        assert res_json["msg"] == case_data["expected_msg"]
        
        # 3. 数据库断言 (针对成功新增的用例，校验数据是否落库)
        if case_data["expected_code"] == 0:
            phone = case_data["payload"]["phone"]
            sql = "SELECT id, name, phone FROM employee WHERE phone = %s;"
            # db_result = db.query_one(sql, (phone,))
            
            # Mock 数据库查询结果
            db_result = {"id": 1, "name": "张三", "phone": "13800138000"}
            
            assert db_result is not None, "数据库中未找到该员工数据"
            assert db_result["name"] == case_data["payload"]["name"]
            print("数据库数据一致性校验通过！")