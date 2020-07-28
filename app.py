from flask import Flask
import os
import subprocess

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def webroot():

    # generate message
    Welcome = "Hello, Miki! Below data is for you!"
    OS_python = "This code is running: " + subprocess.check_output(["python", "--version"], universal_newlines=True)
    OS_name =  "Hostname: " + subprocess.check_output(["hostname"], universal_newlines=True)
    OS_kernel = "Kernel version: " + subprocess.check_output(["uname", "-r"], universal_newlines=True)
    message = Welcome + OS_name + OS_kernel + OS_python
    
    # display it on webpage
    return message #app.send_static_file('./index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
