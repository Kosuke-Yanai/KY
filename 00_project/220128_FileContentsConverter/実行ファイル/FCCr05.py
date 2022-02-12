import os
import shutil
import struct
    
def divide_file(filePath, frame_header_size, chunkSize, chunk_path):
    readedDataSize = frame_header_size
    i = 0
    fileList = []
    # 対象ファイルを開く
    f = open(filePath, "rb")
    # ファイルを読み終わるまで繰り返す
    contentLength = os.path.getsize(filePath)
    while readedDataSize < contentLength:
        # 読み取り位置をシーク
        f.seek(readedDataSize)
        # 指定されたデータサイズだけ読み込む
        data = f.read(chunkSize)
        # 分割ファイルを保存
        saveFilePath = chunk_path + "/" + filePath + "." + str(i)
        with open(saveFilePath, 'wb') as saveFile:
            saveFile.write(data)
        # 読み込んだデータサイズの更新
        readedDataSize = readedDataSize + len(data)
        i = i + 1
        fileList.append(saveFilePath)
    return fileList

def check_string(filePath, timestamp):
    with open(filePath, 'rb') as temp_f:
        if timestamp in temp_f.read():
            return True # The string is found
        return False  # The string does not exist in the file

def FCC(filePath, frame_header_size, line_header_size, line_data_size,                 target_unitID, target_timestamp, target_from, target_to):
    write_data = b''
    # メイン処理
    with open(filePath, 'rb') as fr:
#         frame_header = fr.read(frame_header_size) #先頭4byteはスキップ  
#         write_data = frame_header
        while True:
            line_header_data = fr.read(line_header_size)
            line_main_data = fr.read(line_data_size)

            if line_header_data[5:6] == target_unitID and line_header_data[8:12] == target_timestamp and             line_header_data[4:5] == target_from:
                line_header_replaced = line_header_data[4:5].replace(target_from, target_to)
            else:
                line_header_replaced = line_header_data[4:5]
            write_data += (line_header_data[0:4] + line_header_replaced + line_header_data[5:12] + line_main_data)

            if line_header_data == b'' or line_main_data == b'':
#                 print('End of File')
                break
        # 置換結果でファイル上書き
        fw = open(filePath, 'wb')
        fw.write(write_data) 
        fw.close()
        fr.close()

def join_file(file_list, filePath):
    with open(filePath, 'wb') as saveFile:
        saveFile.write(b'\xEF\xBE\xAD\xDE')
        for f in file_list:
            data = open(f, 'rb').read()
            saveFile.write(data)
            saveFile.flush()

def main():

    # 初期化
    frame_header_size = 4 # DEADBEEF
    line_header_size = 12 # ラインデータのヘッダ部 12
    line_data_size = 1280 # ラインデータ本体 1280
    chunk_size = (line_header_size + line_data_size) * 200 * 8 * 1 # ファイル分割サイズ 8ch x 1frm
    
    input_file = 'input.DMP'
    output_file = './output.DMP' 
    chunk_path = './chunk_data'
    output_data = b''
    count = 0
    
    os.mkdir(chunk_path)
    
    #データ入力
    target_unitID = int(input('Enter target_unitID:')).to_bytes(1, 'little')
    target_timestamp = int(input('Enter timestamp:')).to_bytes(4, 'big') # 67438087
    target_from = int(input('Enter angleID From:')).to_bytes(1, 'little')
    target_to = int(input('Enter angleID To:')).to_bytes(1, 'little')

    # ファイル分割
    file_list = divide_file(input_file, frame_header_size, chunk_size, chunk_path)
    
    # ファイル捜査しhitしたら置換処理を行う
    for filePath in file_list:
        count += 1
        print('Progress: ', count, '/', (len(file_list))) if count%5 == 0 else 'odd'
        result = check_string(filePath, target_timestamp) # ファイル捜査
        if result: # hitしたものに対し置換処理
            FCC(filePath, frame_header_size, line_header_size, line_data_size,                 target_unitID, target_timestamp, target_from, target_to)
    
    # 分割したファイルを結合する
    join_file(file_list, output_file)
    
    shutil.rmtree(chunk_path)
    
    input("処理完了しました。キー入力待ち。 ")
            
if __name__ == "__main__":
    main()
