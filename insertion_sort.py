def insertion_sort(data):
    n = len(data)
    for i in range(1, n):#1から最後までループ
        j = i 
        #jが0より小さく、左隣より小さい場合
        while j > 0 and data[j] < data[j - 1]:
            #左隣と値を交換
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1 #対象を左に移動
    return data

# 動作確認
if __name__ == "__main__":
    import random
    test_data = random.sample(range(20), k=10)
    print('test data=', test_data)
    sorted_data = insertion_sort(test_data)
    print('sorted data=', sorted_data)
