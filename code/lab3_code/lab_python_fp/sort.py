def sort(data):
    print('Unsorted:')
    print(data)

    print('Sorted by abs descending')
    sorted_data = sorted(data, key=abs, reverse=True)
    print(sorted_data)

    print('Sorted by abs descending with lambda')
    sorted_with_lambda_data = sorted(data, key=lambda d: abs(d), reverse=True)
    print(sorted_with_lambda_data)
