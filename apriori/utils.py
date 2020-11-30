from collections import defaultdict

def get_apriori(dataset, pair_size = 2, threshold = 3):
    # create dict
    pairs = defaultdict(int)

    for row in dataset:
        for idx, item in enumerate(row):
            if idx + pair_size >= len(row):
                continue

            # add items to key
            if pair_size > 1:
                row_slice = row[idx:idx + pair_size]
                combination = []
                for i in row_slice:
                    combination.append(i)
                key = str(combination)
                pairs[key] += 1
            else:
                pairs[item] += 1

    threshold_pairs = defaultdict(int)
    for k,v in pairs.items():
        if v >= threshold:
            threshold_pairs[k] = v
    return threshold_pairs



