import json

def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def find_value_by_id(values, test_id):
    for value in values:
        if value['id'] == test_id:
            return value['value']
    return None

def update_test_values(tests, values):
    for test in tests:
        test_value = find_value_by_id(values, test['id'])
        if test_value is not None:
            test['value'] = test_value
        if 'values' in test:
            update_test_values(test['values'], values)

def main(tests_file, values_file, report_file):
    tests_data = load_json_data(tests_file)
    values_data = load_json_data(values_file)['values']
    
    update_test_values(tests_data['tests'], values_data)
    
    with open(report_file, 'w') as file:
        json.dump(tests_data, file, indent=4)

# Здесь укажите пути к файлам
main('tests.json', 'values.json', 'report.json')
