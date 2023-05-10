# cdn
# Allure report:
1. Install the Allure command-line tool by following the instructions on their website: https://docs.qameta.io/allure/
2. Install the pytest-allure-adaptor library by running the following command in your terminal:
pip install pytest-allure-adaptor
3. In your pytest configuration file (typically called pytest.ini), add the following lines:
[pytest]
addopts = --alluredir=<path_to_allure_results>



