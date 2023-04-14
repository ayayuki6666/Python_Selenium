import os

import pytest

if __name__ == '__main__':
    pytest.main()
    os.system("D:\Software\\1.Tools\\allure\\bin\\allure generate ./allure_results -o ./allure_reports --clean")
    os.system("D:\Software\\1.Tools\\allure\\bin\\allure open ./allure_reports")