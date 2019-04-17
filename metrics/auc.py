from sklearn.metrics import roc_auc_score

def my_auc(y_true, y_pre):
    helper = []
    n = len(y_true)
    count_pos = 0
    for i in range(n):
        if y_true[i] == 1:
            count_pos += 1
        helper.append([y_true[i], y_pre[i]])
    count_neg = n - count_pos
    if count_pos == 0 or count_neg == 0:
        return 0
    helper.sort(key=lambda x: x[1], reverse=True)
    pre = [0, 0]
    res = 0
    n_pos, n_neg = 0, 0
    for i in range(n):
        if helper[i][0] == 0:
            n_neg += 1
        else:
            n_pos += 1
        res += (n_neg / count_neg - pre[0]) * (pre[1])
        pre = [n_neg / count_neg, n_pos / count_pos]
    return res


if __name__ == '__main__':
    y_true = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    y_pre = [0.9, 0.8, 0.7, 0.5, 0.6, 0.65, 0.55, 0.3, 0.2, 0.1]
    print("my auc:", my_auc(y_true, y_pre))
    print("sklearn auc:", roc_auc_score(y_true, y_pre))

```
output:
my auc: 0.88
sklearn auc: 0.88
```
