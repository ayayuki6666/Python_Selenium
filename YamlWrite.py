import datetime
import yaml
file = "Test_03/data/login.yaml"
dump=[]
for i in range(4):
    now = datetime.datetime.now()
    Time = now.strftime("%Y-%m-%d %H:%M:%S")
    account={"account": str(i+1), "password": "Test:"+str(i+1)+" "+Time,"expected":True}
    dump.append(account)
print(dump)
with open(file,"w",encoding='utf-8') as f:
    yaml.dump(dump,f,allow_unicode='utf-8')
