import time, random, requests, mysql.connector, csv
import DAN
import numpy as np
import pandas as pd
import aiq_mysql

ServerURL = 'https://aiqtalk.aiqsmartclothing.com/'     #with non-secure connection;
#ServerURL = 'https://YourServerDomainName' #with SSL connection 若用 IP 則無法用 https://
Reg_addr = "AiQ_db"  #None #if None, Reg_addr = MAC address(會用 UUID, 一部機器只能跑一份)
##    上列要改以免與別人衝到 ! 如像原版給 None 則在 DAN.py 內會用 UUID, 這樣一部電腦只能跑一份這程式
DAN.profile['dm_name']='AiQ'    ##  What are you? 你是啥東東
DAN.profile['df_list']=['BT-I','DongleID-I','GatewayID-I','HR-I','Power-I','RR-I']   ##  你有哪些功能, 包括 IDF 和 ODF
DAN.profile['d_name']= 'AiQ_db'       ##  who are you? 你是誰
DAN.device_registration_with_retry(ServerURL, Reg_addr)
r = requests.post('http://aiqtalk.aiqsmartclothing.com:8883//api/v0/project/41/deviceobject/121/device/bind/541/')
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

while True:
    try:
        data = aiq_mysql.sql_get()
        for row in data:
            if row[2] == "483A18784939": #判斷哪個reader上傳
                DAN.push('BT-I', str(row[14])) #對應DF將資料上傳
                DAN.push('DongleID-I', str(row[0])) #對應DF將資料上傳
                DAN.push('GatewayID-I', str(row[2])) #對應DF將資料上傳
                DAN.push('HR-I', str(row[10])) #對應DF將資料上傳
                DAN.push('Power-I', str(row[7])) #對應DF將資料上傳
                DAN.push('RR-I', str(row[13])) #對應DF將資料上傳



    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)