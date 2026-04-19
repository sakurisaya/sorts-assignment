from collections import deque

def merge_sort(data):
    # 要素が1つ以下なら分割終了
    n = len(data)
    if n <= 1:
        return data
    
    # 左右に分割
    mid = n // 2
    left = merge_sort(data[:mid]) # 左側をさらに分割
    right = merge_sort(data[mid:]) # 右側をさらに分割
    # 分割されたグループを合体
    return merge(left, right)

def merge(left, right):
    # リストをdequeに変換
    left_q = deque(left)
    right_q = deque(right)
    result = []
    # 左右両方に数字が残っている間ループ
    while left_q and right_q:
        # 安定ソートのため左側を優先
        if left_q[0] <= right_q[0]:
            result.append(left_q.popleft())
        else:
            result.append(right_q.popleft())
    # 片方の箱が空になったら、残っている数字をすべて追加
    result.extend(left_q)
    result.extend(right_q)
    
    return result

# 動作確認
if __name__ == "__main__":
    import random
    test_data = random.sample(range(20), k=10)
    print('test data=', test_data)
    sorted_data = merge_sort(test_data)
    print('sorted data=', sorted_data)

