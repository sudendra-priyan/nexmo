import os
import yaml
import pytest


def pytest_addoption(parser):
    """
    Fetches custom pytest variable  from CLI
    """
    parser.addoption("--env", action="store", required=True, default=False,
                     help="Environment arguments. Eg: --env uat or --env local,uat ")


def pytest_configure(config):
    """
    Prerequisites which needs to done in Before Suite

    """
    print("\nBefore Suite")

    env = config.getoption("--env")
    env = env.replace(" ", "")
    supported_environment = ["dev", "production"]

    print("Selected Environment", env)
    if env.lower() in supported_environment:
        os.environ["environment"] = env
    else:
        pytest.xfail(f"Invalid Environment has been passed - {env}")

    yaml_file = open("./config.yaml")
    parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
    os.environ["jwt_token"] = parsed_yaml_file['app_config']['jwt']
