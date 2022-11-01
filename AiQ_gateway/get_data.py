import re
import socket

def get():
    bind_ip = "192.168.1.110"   #設定本地主機IP
    bind_port = 6001    #聽取IP的PORT號
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #TCP宣告方式

    server.bind((bind_ip,bind_port))    #設定需監聽IP與Port號
    server.listen(5)    #伺服器Socket接收最大量
    print("[*] Listening on %s %d " % (bind_ip, bind_port))  # 顯示正在監聽的IP與Port
    while True:
        try:
            client,addr = server.accept()   #伺服器接受串接，並回傳IP與資訊
            print('Connected by ',addr) #顯示以連接裝置IP
            while True:
                data = client.recv(79)  #TCP接資料函示(宣告接收最大數值)
                data = data.decode()    #將資料做解碼(預設為解碼成字串)
                data2list = data.split(',') #將字串分割儲存至陣列

                if data2list[0] == "$F0": #判斷是否為Sensor資料
                    Gateway = data2list[1] #reader ID
                    Dongle = data2list[3] #tag ID
                    inf = data2list[7] # tag data
                    inf_data = re.findall(r'.{2}',inf) #由於tag data是2字元資料串，以每兩位元分割儲存至另一個陣列
                    pow = str(int(inf_data[3],16)) # Battery power
                    HR = str(int(inf_data[6],16))   # Heart Rate
                    BR = str(int(inf_data[9],16))   # Breath Rate
                    BT = str(int(inf_data[10],16)/10+20)    # BodyTemperture
                    redata = Dongle+','+Gateway+','+BT+','+HR+','+pow+','+BR # 將資料透過逗號串聯起來
                    print(redata)
                    return redata
        except:
            print(socket.error)
get()