from flask import Flask 
from flask_restful import Api, Resource
import subprocess
import json


def get_cpu():
    # cpu:
    cpu_vendor = str(subprocess.getoutput('cat /proc/cpuinfo | grep "vendor_id" | uniq').split(":")[1])
    cpu_model = str(subprocess.getoutput('cat /proc/cpuinfo | grep "model name" | uniq').split(":")[1])
    cpu_cores = str(subprocess.getoutput('cat /proc/cpuinfo | grep "cpu cores" | uniq').split(":")[1])

    cpudict = dict(cpuvendor=cpu_vendor, cpumodel=cpu_model, cpucores=cpu_cores)
    #print(json.dumps(cpudict))
    return json.dumps(cpudict)

def get_mem():
    # memory:
    mem_total = str(subprocess.getoutput('cat /proc/meminfo | grep "MemTotal" | uniq | tr -s [:blank:]').split(":")[1])
    mem_free = str(subprocess.getoutput('cat /proc/meminfo | grep "MemFree" | uniq | tr -s [:blank:]').split(":")[1])
    swap_total = str(subprocess.getoutput('cat /proc/meminfo | grep "SwapTotal" | uniq | tr -s [:blank:]').split(":")[1])
    swap_free = str(subprocess.getoutput('cat /proc/meminfo | grep "SwapFree" | uniq | tr -s [:blank:]').split(":")[1])

    memdict = dict(memorytotal=mem_total, memfree=mem_free, swaptotal=swap_total, swapfree=swap_free)
    #print(json.dumps(memdict))
    return json.dumps(memdict)

def get_net():
    # how people sees us
    net_info = subprocess.getoutput('curl -s ifconfig.me/all.json')
    #print(net_info)
    return net_info

def get_os():
    # os info
    os_os = str(subprocess.getoutput('uname -o'))
    os_kernel = str(subprocess.getoutput('uname -r'))
    os_hw = str(subprocess.getoutput('uname -i'))
    os_proc = str(subprocess.getoutput('uname -p'))
    os_node = str(subprocess.getoutput('uname -n'))

    osdict = dict(os=os_os, kernel=os_kernel, hw=os_hw, proc=os_proc, node=os_node)
    #print(json.dumps(osdict))
    return json.dumps(osdict)

def default(message):
    return {"message ": message}


app = Flask(__name__)
api = Api(app)

@app.route('/')
def root():
    supported = "os|OS|mem|MEM|net|NET|cpu|CPU"
    return default(supported)

@app.route('/<string:req>', methods=['GET', 'POST'])
def get_info(req):
    supported = "os|OS|mem|MEM|net|NET|cpu|CPU"
    if req.lower() == 'cpu': return get_cpu()
    if req.lower() == 'mem': return get_mem()
    if req.lower() == 'net': return get_net()
    if req.lower() == 'os': return get_os()
    if req not in supported: return default(supported)


if __name__ == "__main__":
    #app.run(debug=True, host='127.0.0.1', port=5000)
    app.run(host='0.0.0.0', port=5000)
