print("HTTP/1.0 200 OK\n")
import cgi
form = cgi.FieldStorage()
f_name=form["f_name"].value
s_name=form["s_name"].value
r1=form["r1"].value
my_class=form["class"].value


print("<br><b>First Name</b>",f_name)
print("<br><b>Second Name</b>",s_name)
print("<br><b>Sex</b>",r1)
print("<br><b>Class</b>",my_class)
print("<br><br><br><a href=form.htm>Back to Form</a>")