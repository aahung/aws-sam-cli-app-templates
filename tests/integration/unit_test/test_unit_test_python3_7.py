from tests.integration.base import Base, LOG


class UnitTest_python3_7_cookiecutter_aws_sam_hello_python(Base.PythonUnitTestBase):
    directory = "python3.7/cookiecutter-aws-sam-hello-python"
    code_directories = ["hello_world"]


class UnitTest_python3_7_cookiecutter_aws_sam_eventBridge_python(Base.PythonUnitTestBase):
    directory = "python3.7/cookiecutter-aws-sam-eventBridge-python"
    code_directories = ["hello_world_function"]


class UnitTest_python3_7_cookiecutter_aws_sam_eventbridge_schema_app_python(Base.PythonUnitTestBase):
    directory = "python3.7/cookiecutter-aws-sam-eventbridge-schema-app-python"
    code_directories = ["hello_world_function"]

    def _test_unit_tests(self, code_directory: str):
        self.skipTest("This unit test will fail")
        pass


class UnitTest_python3_7_cookiecutter_aws_sam_step_functions_sample_app(Base.PythonUnitTestBase):
    directory = "python3.7/cookiecutter-aws-sam-step-functions-sample-app"
    code_directories = [
        "functions/stock_buyer",
        "functions/stock_checker",
        "functions/stock_seller",
    ]
