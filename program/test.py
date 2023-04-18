# 统计数量(test)：
import yaml


def print_info(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        result = yaml.safe_load(f)
        print(file_name + "\t" + str(len(result)))
        if file_name == "output/result.yml":
            total_number = 0
            for key in result:
                total_number = total_number + int(result[key]['number'])
                # print(result[key])
            print(file_name + "\t" + str(total_number))
            
        if file_name == "output/classification_data.yml":
            total_number = 0
            for key in result:
                # print(result[key]['number'])
                total_number = total_number + int(result[key]['number'])
            print(file_name + "\t" + str(total_number))
        # for key in result:
        #     print( " - " +  str(key['cwe_id']))
    
# file_name = "sources/software.yml"
# file_name = "sources/cwe_info.yml"
# file_name = "output/result.yml"
file_name = "output/classification_data.yml"
print_info(file_name)


