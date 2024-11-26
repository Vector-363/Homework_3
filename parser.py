from evaluator import evaluate_expression


def parse_config(yaml_data):
    result = ""
    for key, value in yaml_data.items():
        if isinstance(value, dict):
            result += f"$[\n{parse_config(value)}\n]\n"
        elif isinstance(value, list):
            result += f"array({', '.join(map(str, value))})\n"
        elif isinstance(value, str) and value.startswith("!"):
            result += f"{evaluate_expression(value[1:])}\n"
        else:
            result += f"{key} is {value}\n"
    return result

