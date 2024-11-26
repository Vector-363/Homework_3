from evaluator import evaluate_expression
import re

def parse_config(yaml_data, context={}):
    result = ""
    for key, value in yaml_data.items():
        if isinstance(value, dict):
            result += f"$[\n{parse_config(value, context)}\n]\n"
        elif isinstance(value, list):
            items = [str(item) for item in value] # упростили обработку списков
            result += f"array({', '.join(items)})\n"
        elif isinstance(value, str) and value.startswith("!"):
            #обработка ошибок в выражениях
            try:
              res = evaluate_expression(value[1:], context)
              if isinstance(res, str) and "Ошибка" in res:
                raise ValueError(res) #перебрасываем ошибку дальше
              result += f"{key} is {res}\n"
            except ValueError as e:
              raise ValueError(f"Ошибка вычисления выражения '{value}': {e}") #более информативное сообщение об ошибке
        elif isinstance(value, str) and re.match(r"^\s*'", value): #Проверка на комментарий
          continue # пропускаем строку, если это комментарий
        else:
            context[key] = value
            result += f"{key} is {value}\n"
    return result





