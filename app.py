import psutil
from flask import Flask

app= Flask(__name__)

@app.route("/")

def index():
    cpu_percent=psutil.cpu_percent()
    mem_per=psutil.virtual_memory().percent
    message=None
    
    if cpu_percent >80 or mem_per > 80 :
        message= f'high memory and cpu ultization'
        
    return f'cpu_percent {cpu_percent},mem_per{mem_per}'

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')