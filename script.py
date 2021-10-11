def func(n1, n2):
    return (n1 * (n2 + 6) % 27) + 1


def main():
    your_variant = 10
    for n1 in range(1, 5):
        with open(f'{n1}.txt') as f:
            for n2, name in enumerate(f.readlines()):
                if func(n1, n2 + 1) == your_variant:
                    print(f'{n1} {name}')


if __name__ == '__main__':
    main()
