


#ビット全探索
#iは数字の選び方
i = 1

for j in range(3):
 print(str(j) + '回目')
 #(1 << N) は 2 の N 乗
 #2進数の下位桁を表す
 #2^0 0001
 #2^1 0010
 print (bin(1 << j))
# iの各桁を & 論理積で取り出す
 print(bin(i & 1<<j))
#!= 2つの値がイコールでない時に「正」
# i = 1
#    0001 i
#   &0001 1 << j
#       1
#   1 != 0 true
 print ((i & (1 << j)) != 0)
 