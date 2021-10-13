import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    # Trying to read coefficient from console arguments.
    if (len(sys.argv) > index): 
        coef_str = sys.argv[index]
    else:
        # Otherwise entering it manually.
        print(prompt)
        coef_str = input()
    # Conversion.
    try:
        coef = float(coef_str)
    # Input wasn't a float number.
    except:
        print('Число было введёно неверно!')
        print(prompt)
        return get_coef(index, prompt);

    return coef


def get_bisquare_roots(a, b ,c):
    result = []

    squared_result = get_square_roots(a, b, c)

    for squared_root in squared_result:
        if squared_root < 0:
            continue;

        if squared_root == 0:
            result.append(squared_root)
        elif squared_root > 0:
            root = math.sqrt(squared_root)
            result.append(-root)

    return result


def get_square_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
        '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_bisquare_roots(a,b,c)
    # Вывод корней
    if not len(roots):
        print('Нет корней')
    for root in roots:
        print(root)
    # len_roots = len(roots)
    # if len_roots == 0:
        # print('Нет корней')
    # elif len_roots == 1:
        # print('Один корень: {}'.format(roots[0]))
    # elif len_roots == 2:
        # print('Два корня: {} и {}'.format(roots[0], roots[1]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
