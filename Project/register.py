#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print "Register Here"
print """
<html>
<head>
</head>
<body>
<h1>Registration Page</h1>
<form action="code.py" method="post">
Name
<input type="text" name="name"/>
<br/>
F'Name
<input type="text" name="fname"/>
<br/>
Gender
<input type="radio" name="a" value="male"/>Male
<input type="radio" name="a" value="female"/>Female
<br/>
Email
<input type="email" name="email"/>
<br/>
Password
<input type="password" name="password"/>
<br/>
<input type="submit"/>
</form>
</body>
</html>




"""