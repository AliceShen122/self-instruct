import json

def load_jsonl(file_path):
    data = []
    with open(file_path,'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            json_obj = json.loads(line)
            data.append(json_obj)
    return data

# 读取JSONL文件
file_path = 'F:/projects/self-instruct/data/gpt3_generations/machine_generated_instances.jsonl'
test=[json.loads(l) for l in open(file_path,'r',encoding='utf-8')]
print("end")