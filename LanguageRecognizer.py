import re
fileName = input("Enter file name: ")

if fileName[-3:]=='txt':
    
    f = open(fileName).read()

    regex_java = re.compile("(public |private |protected |default )?[\s]class[\s]+[A-Z]+[\w]*{[\s\w;/*=+-]*public[\s]+static[\s]*void[\s]*main[\s]*[(]String[\s]+[\w]+[[]?[]]?[)][\s\w]*{")           
    regex_cpp_java = re.compile("class[\s][A-Z]+[\w]*{[\s\w;/*=+-]*[}]");

    regex_c = re.compile("([\s]*#[\s]*include[\s]*[<\"][\w]*.h[\">][\s]*){2,}")
    regex_c1 = re.compile("(int |void |char |float |double )[\s]*main[(][\w]*[)]")
    regex_io1 = re.compile("[{](printf|scanf)[}]")
    regex_io2 = re.compile("(cout[\s]*<<[\s]*|cin[\s]*>>[\s]*)")

    regex_html = re.compile("[\s\w;/*<>=!+-]*<[\s]*html[\s\w;/*=!+-]*>[\s\w]*<[\s]*title[\s\w;/*=!+-]*>[\s\w]*<[\s]*/title[\s]*>[\s\w;/*<>=!+-]*<[\s]*body[\s\w;/*=!+-]*>[\s\w;/*<>.=!+-]*<[\s]*/body[\s]*>[\s\w;/*<>.=!+-]*<[\s]*/html[\s]*>[\s]*")





    if regex_java.search(f) is not None:
    #     print(regex_java.search(f).group())
        print("Given Program is written in Java")

    elif regex_c.search(f) is not None:
        
        if regex_c1.search(f) is not None:

            if regex_io1.search(f) is not None:
                print("Given Program is written in C")
            elif regex_io2.search(f) is not None:
                print("Given Program is written in C++")
            else:
                print("Given Program is written in either C or C++")
        else :
            print("Given Program is written in either C or C++")
    # int("Given Program is written in C family language")

    elif regex_html.search(f) is not None:
    #     print(regex_html.search(f).group())
        print("Given Program is written in html")
    elif regex_cpp_java.search(f) is not None:
        print("Given Program is written in either Java or C++")
    else:
        print("Sorry!!! Language unrecognizable");
    
else:
    print("Entered file is not text file")



