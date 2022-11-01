##DAI.py #coding=utf-8 -- 注意這原版 Dummy_Device 沒指定 Reg_addr 會使用 UUID (在 DAN.py內)
import time, random, requests, csv, re, socket
import DAN
import numpy as np
import pandas as pd
import get_data #引用程式

ServerURL = 'https://aiqtalk.aiqsmartclothing.com'     #with non-secure connection;
#ServerURL = 'https://YourServerDomainName' #with SSL connection 若用 IP 則無法用 https://
Reg_addr = "483A18784939"  #None #if None, Reg_addr = MAC address(會用 UUID, 一部機器只能跑一份)
##    上列要改以免與別人衝到 ! 如像原版給 None 則在 DAN.py 內會用 UUID, 這樣一部電腦只能跑一份這程式
DAN.profile['dm_name']='AiQ'    ##  What are you? 你是啥東東
DAN.profile['df_list']=['BT-I','DongleID-I','GatewayID-I','HR-I','Power-I','RR-I']   ##  你有哪些功能, 包括 IDF 和 ODF
DAN.profile['d_name']= '483A18784939'       ##  who are you? 你是誰

DAN.device_registration_with_retry(ServerURL, Reg_addr)

r = requests.post('http://aiqtalk.aiqsmartclothing.com:8883//api/v0/project/41/deviceobject/121/device/bind/541/')
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

while True:
    try:
        data = get_data.get() #使用引用程式函式
        aiq_l = data.split(',') #以逗點切割成在陣列中
        DAN.push('BT-I',aiq_l[2])   #判斷哪個reader上傳
        DAN.push('DongleID-I', aiq_l[0])    #判斷哪個reader上傳
        DAN.push('GatewayID-I', aiq_l[1])   #判斷哪個reader上傳
        DAN.push('HR-I', aiq_l[3])  #判斷哪個reader上傳
        DAN.push('Power-I', aiq_l[4])   #判斷哪個reader上傳
        DAN.push('RR-I', aiq_l[5])  #判斷哪個reader上傳
     
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')