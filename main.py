import argparse
import yaml
from parser import parse_config
import re


def cut_output(input_string):
    return re.sub(r'\{(.*?)\}', r'\1', input_string)


def main():
    parser = argparse.ArgumentParser(description="YAML to ConfigLanguage Converter")
    parser.add_argument("input_file", help="Путь к входному YAML файлу")
    parser.add_argument("output_file", help="Путь к выходному файлу ConfigLanguage")
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r') as f:
            yaml_data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Ошибка: Файл {args.input_file} не найден.")
        return
    except yaml.YAMLError as e:
        print(f"Ошибка парсинга YAML: {e}")
        return

    try:
        config_text = parse_config(yaml_data)
        final_text= cut_output(config_text)
        with open(args.output_file, 'w') as f:
            f.write(final_text)
        print(f"Конфигурация успешно преобразована в {args.output_file}")
    except Exception as e:
        print(f"Ошибка преобразования: {e}")


if __name__ == "__main__":
    main()


