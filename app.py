from flask import Flask, render_template, request
import os
import subprocess

def generate_info_html():
    html_frame = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Info Page</title>
    </head>
    <body>
        <h1>We are running on:</h1>
        <p><b>Hostname:</b> %s</p>
        <p><b>Kernel version:</b> %s</p>
        <p><b>Python version:</b> %s</p>
        <b><p>Click <a href="/">here</a> to go home.</p></b>
    </body>
</html>
"""
    osname =  subprocess.check_output(["hostname"], universal_newlines=False)
    oskernel = subprocess.check_output(["uname", "-r"], universal_newlines=False)
    ospython = subprocess.check_output(["python", "--version"], universal_newlines=False)
    f = open("static/info.html", "w")
    whole = html_frame % (osname, oskernel, ospython)
    f.write(whole)
    f.close()
    
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/info', methods=['GET', 'POST'])
def info():
    generate_info_html()
    return app.send_static_file('info.html')


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 5000)))
