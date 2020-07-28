def client_code():
    pass


if __name__ == '__main__':
    try:
        client_code()
    except ValueError as e:
        print(e)
    except AttributeError as e:
        print(e)
    except Exception as e:
        print(e)
