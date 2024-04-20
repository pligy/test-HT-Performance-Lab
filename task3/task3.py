import sys
import json


def fill_values(tests, values):
    for test in tests:
        for value in values['values']:
            if test['id'] == value['id']:
                test['value'] = value['value']

        if 'values' in test:
            fill_values(test['values'], values)

def get_report(values_path, tests_path, report_path):
    with open(values_path, 'r') as values_file:
        values_data = json.load(values_file)
    with open(tests_path, 'r') as tests_file:
        tests_data = json.load(tests_file)

    fill_values(tests_data['tests'], values_data)

    with open(report_path, 'w') as report_file:
        json.dump(tests_data, report_file, indent=2)

def count_json_files(files):
    count = [1 for file in files if ".json" in file]
    return sum(count)


if __name__ == '__main__':
    try:
        error = "write in the format - python" + \
                "\\path_to_file\\task3.py \\path_to_file\\values.json" + \
                "\\path_to_file\\tests.json \\path_to_file\\report.json"

        if len(sys.argv) != 4:
            raise IOError(error)

        values_path = sys.argv[1]
        tests_path = sys.argv[2]
        report_path = sys.argv[3]

        if count_json_files([values_path, tests_path, report_path]) < 3:
            raise IOError(error)

        get_report(values_path, tests_path, report_path)
    except IOError as ie:
        print("Error:", ie)