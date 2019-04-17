from sklearn.metrics import f1_score

def my_f1_score(y_true, y_pre):
    n = len(y_true)
    tp = 0
    p_pre, p_true = 0, 0
    for i in range(n):
        if y_true[i] == 1 and y_pre[i] == 1:
            tp += 1
        p_true += y_true[i]
        p_pre += y_pre[i]
    recall = tp / p_true
    precission = tp / p_pre
    return 2 * recall * precission / (recall + precission) if recall + precission != 0 else 0

if __name__ == '__main__':
    y_true = [1, 0, 1, 1, 0]
    y_pre = [1, 0, 1, 0, 1]
    print("my f1_score result: ", my_f1_score(y_true, y_pre))
    print("sklearn f1_score result: ", f1_score(y_true, y_pre))

    
```
output:
my f1_score result:  0.6666666666666666
sklearn f1_score result:  0.666666666667
```
