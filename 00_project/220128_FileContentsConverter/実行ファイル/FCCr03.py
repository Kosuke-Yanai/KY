
# #### 06. 【本体】指定byteずつ読み込んだ任意の文字列を置換して出力する

# データイメージ /1byte/
# aa/uu/xx/xx/ts/ts/ts/ts/1280byte data/

import struct

# データ入力
target_unitID = int(input('Enter target_unitID:')).to_bytes(1, 'little')
target_timestamp = int(input('Enter timestamp:')).to_bytes(4, 'big') # 67438087
target_from = int(input('Enter angleID From:')).to_bytes(1, 'little')
target_to = int(input('Enter angleID To:')).to_bytes(1, 'little')

# 初期化
frame_header_size = 4 # DEADBEEF
line_header_size = 8 # ラインデータのヘッダ部
line_data_size = 4 # ラインデータ本体

input_file = './input.DMP'
output_file = './output.DMP'

count = 0
write_data = b''

# メイン処理
with open(input_file, 'rb') as fr:
    frame_header = fr.read(frame_header_size) #先頭4byteはスキップ  
    write_data = frame_header
    while True:
        line_header_data = fr.read(line_header_size)
        line_main_data = fr.read(line_data_size)
        if line_header_data[1:2] == target_unitID and line_header_data[4:8] == target_timestamp and         line_header_data[0:1] == target_from:
            count += 1
            line_header_replaced = line_header_data[0:2].replace(target_from, target_to)
        else:
            line_header_replaced = line_header_data[0:2]
        write_data += (line_header_replaced + line_header_data[2:8] + line_main_data)
        if line_header_data == b'' or line_main_data == b'' :
#             print('End of File')
            break
                  
# ファイル出力
print("置換数:", count)
fw = open(output_file, 'wb')
fw.write(write_data)
fw.close()
fr.close()

input("処理完了しました。キー入力待ち。 ")
