import datetime
import yaml
file = "Test_03/data/like.yaml"
dump=[]
for i in range(2):
    now = datetime.datetime.now()
    Time = now.strftime("%Y-%m-%d %H:%M:%S")
    account={"sequence": str(i+1),"expected":True}
    dump.append(account)
print(dump)
with open(file,"w",encoding='utf-8') as f:
    yaml.dump(dump,f,allow_unicode='utf-8')
