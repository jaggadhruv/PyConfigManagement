import json
import yaml


def read_config_json():
    try:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            return config_data
    except FileNotFoundError:
        print("Error: config.json file is missing")
        return None
    except json.JSONDecodeError:
        print("Error: Unable to parse config.json file")
        return None

def read_config_yaml():
    with open('config2.yaml', 'r') as config_file:
        config_data = yaml.safe_load(config_file)
        return config_data


def main():
    config1 = read_config_json()
    print(config1)

    if config1 is not None:
        param_value_1 = config1['param1']
        param_value_2 = config1['param2']
        param_value_3 = config1['param3']
        param_value_4 = config1['param4']

    print(param_value_1, param_value_2, param_value_3, param_value_4)
    print(type(param_value_1), type(param_value_2), type(param_value_3), type(param_value_4))

    config2 = read_config_yaml()
    print(config2)

    if config2 is not None:
        param_value_5 = config2['param1']
        param_value_6 = config2['param2']
        param_value_7 = config2['param3']

    print(param_value_5, param_value_6,param_value_7)
    print(type(param_value_5), type(param_value_6), type(param_value_7))


if __name__ == "__main__":
    main()