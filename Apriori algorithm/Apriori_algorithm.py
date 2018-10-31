import time

start_time = time.time()


def load_dataset():
    dataset = []
    with open('mushroom.dat') as file:
        for line in file:
            dataset.append(line.split(' ')[:-1])
    return dataset


def create_C1(dataset):
    C1 = set()
    for i in dataset:
        for item in i:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1


def is_apriori(Ck_item, Lk_sub1):
    for i in Ck_item:
        Ck_item_sub = Ck_item - frozenset([i])
        if Ck_item_sub not in Lk_sub1:
            return False
    return True


def create_Ck(Lk_sub1):
    Ck = set()
    len_Lk_sub1 = len(Lk_sub1)
    list_Lk_sub1 = list(Lk_sub1)
    for i in range(len_Lk_sub1):
        for j in range(i + 1, len_Lk_sub1):
            itemset1 = list(list_Lk_sub1[i])
            itemset2 = list(list_Lk_sub1[j])
            itemset1.sort()
            itemset2.sort()
            if itemset1[:-1] == itemset2[:-1]:
                Ck_item = list_Lk_sub1[i] | list_Lk_sub1[j]
                if is_apriori(Ck_item, Lk_sub1):
                    Ck.add(Ck_item)
    return Ck


def generate_Lk_by_Ck(dataset, Ck, min_support, support_data):
    Lk = set()
    item_count = {}
    for i in dataset:
        for Ck_item in Ck:
            if Ck_item.issubset(i):
                if Ck_item in item_count:
                    item_count[Ck_item] += 1
                else:
                    item_count[Ck_item] = 1
    for item in item_count:
        support = item_count[item] / len(dataset)
        if support >= min_support:
            Lk.add(item)
            support_data[item] = support
    return Lk


def generate_final_L(data_set, max_items, min_support):
    support_data = {}
    C1 = create_C1(data_set)
    L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(max_items - 1):
        Ci = create_Ck(Lksub1)
        Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data


def generate_big_rules(L, support_data, min_conf):
    conf_95_100 = 0
    conf_90_95 = 0
    conf_85_90 = 0
    conf_min_85 = 0
    big_rule_list = []
    subset_list = []
    for Lk in L:
        for freq_set in Lk:
            for subset in subset_list:
                if subset.issubset(freq_set):
                    conf = support_data[freq_set] / support_data[subset]

                    if conf >= min_conf:
                        big_rule = (subset, freq_set - subset)
                        big_rule_list.append(big_rule)
                        if conf >= 0.95:
                            conf_95_100 += 1
                        elif conf >= 0.9:
                            conf_90_95 += 1
                        elif conf >= 0.85:
                            conf_85_90 += 1
                        else:
                            conf_min_85 += 1
        subset_list.extend(Lk)

    print('conf_95_100: ' + str(conf_95_100))
    print('conf_90_95: ' + str(conf_90_95))
    print('conf_85_90: ' + str(conf_85_90))
    print('conf_min_85: ' + str(conf_min_85))
    return big_rule_list


L, support_data = generate_final_L(load_dataset(), max_items=5, min_support=0.1)
big_rule_list = generate_big_rules(L, support_data, min_conf=0.8)

for i in range(5):
    print('L[{}]: '.format(i) + str(len(L[i])))
print('共找到 {} 滿足條件的規則'.format(len(big_rule_list)))
print('處理程序耗時: {} 秒'.format(time.time() - start_time))

with open('output.txt', 'w') as out:
    for i in big_rule_list:
        out.write(str(i[0]) + '=>' + str(i[1]) + '\n')
    out.write('處理程序耗時: {} 秒'.format(time.time() - start_time))
# conf_95_100: 262480
# conf_90_95: 50911
# conf_85_90: 37867
# conf_min_85: 42415
# L[0]: 56
# L[1]: 763
# L[2]: 4593
# L[3]: 16150
# L[4]: 38800
# 共找到 393673 滿足條件的規則
# 處理程序耗時: 814.9624228477478 秒
