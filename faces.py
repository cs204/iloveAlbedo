def main():
    s =input( )
    s2 = convert(s)
    print(s2)


def convert(s):
    s2 = s.replace(":)", "\N{Slightly Smiling Face}")
    s4 = s2.replace(":(", "\N{Slightly Frowning Face}")
    return s4


main( )