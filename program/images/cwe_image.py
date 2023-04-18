import matplotlib.pyplot as plt
import yaml
from functools import partial

labels = []
sizes = []

# 定义函数读取数据
def get_file_info(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        result = yaml.safe_load(f)
        print(file_name + "\t" + str(len(result)))
        if file_name == "output/cwe_result.yml":
            for key in result:
                labels.append(key)
                sizes.append(len(result[key]))

# 调用函数读取数据
get_file_info("output/cwe_result.yml")

# 根据size对标签进行排序
sort_func = partial(sorted, key=lambda x: -x[1])
sorted_data = sort_func(zip(labels, sizes))

# 取出size最多的前6个标签和数据
important_labels = [label for label, size in sorted_data[:5]]
important_sizes = [size for label, size in sorted_data[:5]]

# 将剩余标签和数据合并为“其他”
other_size = sum(size for label, size in sorted_data[5:])
other_label = "Other"
important_sizes.append(other_size)
important_labels.append(other_label)

# 绘制饼图
fig, ax = plt.subplots(figsize=(6, 5))
wedgeprops = {"width": 0.6, "edgecolor": "white", "linewidth": 2}
ax.pie(important_sizes, labels=important_labels, autopct="%1.1f%%", startangle=90,
       wedgeprops=wedgeprops, textprops={"fontsize": 8})
ax.set_title("Crypto CWE - Vuln Info")

# plt.show()
plt.savefig('output/images/Crytpo_CWE.svg', format='svg')
