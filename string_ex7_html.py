def get_title():
    title = raw_input("Enter html title : ")
    return title

def get_heading1():
    main = raw_input("Enter main heading : ")
    return main

def get_heading2():
    sub = raw_input("Enter sub heading : ")
    return sub

def get_para1():
    paragraph1 = raw_input("Enter paragraph_1 : ")
    return paragraph1

def get_para2():
    paragraph2 = raw_input("Enter paragraph_2 : ")
    return paragraph2

def build_html(title, main, sub, para1, para2):
    print"-" * 70
    print"<html>"
    print"<title>", title, "</title>"
    print"<body>"
    print"<h1>", main, "</h1>"
    print"<h2>", sub, "</h2>"
    print"<p>", para1, "</p>"
    print"<p>", para2, "</p>"
    print"</body>"
    print"</html>"
    print"-" * 70

title = get_title()
main = get_heading1()
sub = get_heading2()
para1 = get_para1()
para2 = get_para2()
build_html(title, main, sub, para1, para2)

