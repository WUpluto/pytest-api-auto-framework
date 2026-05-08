# 企业级接口自动化测试框架 (Pytest + Requests)

## 项目简介
本项目为企业中后台管理系统量身定制的接口自动化测试框架，实现了数据与业务逻辑解耦，并集成了完整的鉴权机制与数据库校验。

## 核心技术栈
* **Python 3.x**
* **Pytest**: 测试框架与用例管理
* **Requests**: HTTP 接口调用
* **PyYAML**: YAML 文件实现数据驱动 (DDT)
* **PyMySQL**: 连接 MySQL 进行数据一致性落库断言
* **Allure**: 生成可视化测试报告

## 亮点功能
1. 利用 Pytest `conftest.py` 的 `fixture` 机制处理登录 Token 依赖，实现一次登录，全局会话保持。
2. 引入二次断言机制：不仅校验 HTTP 状态码与 JSON 业务码，更通过 MySQL 校验关键业务数据的落库正确性。