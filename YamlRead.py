import yaml
def read(path):
    with open(path,'r') as file:
        data=file.read()
        result =yaml.load(data,Loader=yaml.FullLoader)
        return result

if __name__ == '__main__':
    result=read("Test_03/data/post.yaml")
    print(result)