def main():
    try:
        configuration = open('C:\Users\crist\Documents\CURSO_PYTHON\MODULO10\config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()