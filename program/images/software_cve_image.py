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
        if file_name == "output/result.yml":
            for key in result:
              if key == "crypto":
                     continue
              labels.append(key)
              sizes.append(int(result[key]['number']))

# 调用函数读取数据
get_file_info("output/result.yml")

# 根据size对标签进行排序
sort_func = partial(sorted, key=lambda x: -x[1])
sorted_data = sort_func(zip(labels, sizes))

appropriate_size = 15

# 取出size最多的前6个标签和数据
important_labels = [label for label, size in sorted_data[:appropriate_size]]
important_sizes = [size for label, size in sorted_data[:appropriate_size]]

# 将剩余标签和数据合并为“其他”
other_size = sum(size for label, size in sorted_data[appropriate_size:])
other_label = "Other"
important_sizes.append(other_size)
important_labels.append(other_label)

# 绘制柱状图
fig, ax = plt.subplots(figsize=(7, 8))
ax.bar(range(len(important_labels)), important_sizes)
ax.set_xticks(range(len(important_labels)))
# plt.xticks(rotation=90, fontsize=8)
ax.set_xticklabels(important_labels, rotation=15, ha='right', fontsize=8)
ax.set_ylabel("CVE Number")
ax.set_xlabel("Crypto Libs")
ax.set_title("Crytpo Libs' CVE")

# plt.show()
plt.savefig('output/images/Crytpo_Libs_CVE.svg', format='svg')
