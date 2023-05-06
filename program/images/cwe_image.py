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

# 取得标签描述
label_desc = {
    'CWE-310' : '与数据机密性和完整性的设计和实现有关。\n通常涉及使用加密技术、加密库和哈希算法',
    'CWE-326' : '产品使用的加密方案理论上来说是可行的，\n但所需的保护级别上并不足够强大',
    'CWE-327' : '使用了一个有缺陷的或危险的加密算法或协议',
    'CWE-330' : '由于产品在安全相关的上下文中使用了不充分随机的数字或值。',
    'CWE-347' : '产品不验证或错误地验证数据的加密签名',
    'Other': '其他密码学问题'
    }

new_labels = [label for label in important_labels]

# 绘制饼图
fig, ax = plt.subplots(figsize=(15, 6))
wedgeprops = {"width": 0.6, "edgecolor": "white", "linewidth": 1}
ax.pie(important_sizes, labels=new_labels, autopct="%1.1f%%", startangle=90,
       wedgeprops=wedgeprops, textprops={"fontsize": 8})
ax.set_title("Crypto CWE - Vuln Info")


# 添加legend
legend_labels = [f"{label.split()[0]} - {label_desc.get(label.split()[0], '')}" for label in sorted(set(new_labels))]
ax.legend(legend_labels, bbox_to_anchor=(1.5, 1.0), loc='upper center', fontsize=8)

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 尝试添加引导线
# https://blog.csdn.net/mighty13/article/details/116010035

# 保存并展示图像
plt.savefig('output/images/Crytpo_CWE.svg', dpi=300, format='svg')
# plt.show()