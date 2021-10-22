from helpers import get_warnings, get_current_time


def main():
    url = "https://zh.stwarn.ch/"
    filename = 'sturmwarnung_log.txt'
    warnings = get_warnings(url)

    with open(filename, 'a') as file:
        file.write(get_current_time() + '\n')
        file.write('\n'.join('%s %s' % x for x in warnings) + '\n')


if __name__ == '__main__':
    main()
