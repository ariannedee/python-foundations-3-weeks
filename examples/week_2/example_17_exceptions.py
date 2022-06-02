try:
    int('five')  # raises ValueError
    print('Success!')  # doesn't print
except ValueError as e:
    print("Fail!")  # prints
    print(e)  # captured exception


print('Got here')

int('1.5')  # Run fails with exit code 1
print("Didn't get here")  # doesn't print
