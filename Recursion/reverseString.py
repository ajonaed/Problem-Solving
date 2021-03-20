def reverse_String(s):
    if len(s) == 0:
        return s
    else:
        result = reverse_String(s[1:]) + s[0]
        return result

def main():
    s = 'USA'
    print(reverse_String(s))


if __name__ == '__main__':
    main()
