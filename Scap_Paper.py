import webbrowser

newPage = open("newpage.txt", "w")#Link a variable with a newly created file with the specified name, if it does not exist already..
##The following will write a basic HTML template into the new file
newPage.write("""

<!DOCTYPE html>
<html lang ='en'>  
<head>     
                <title>Stay Tuned</title>
                <meta charset = "utf-8">
</head>  
<body> 
                        <p>Stay tuned for more details!</p>
</body>  
</html>

""")

newPage.close()#Close the file we opened/created because were not changing it right now 