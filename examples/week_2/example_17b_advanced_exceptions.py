try:
    int('5')
    print('Success!')
    print(hi)
except (ValueError, NameError) as e:  # Catch multiple error types
    print("Fail!")
    print(repr(e))


try:
    int('5')
    print('Success!')
    print(hi)
except ValueError:  # Catch multiple error types with different behaviour
    print("Failure: Value error")
except NameError:
    print("Failure: Name error")


try:
    int('5')
except ValueError:
    print("Fail!")
else:
    print('Success!')  # Runs after try block finishes without errors
finally:
    print('This always happens')  # Runs after everything, even if there was an error



class MyException(Exception):
    pass


raise MyException("error message")
