import load_data as pipe
import os
import sqlite3


def test_get_request(url,output):
    success = pipe.get_request(url,output)
    if success:
        print(f"success {url}")
    else:
        print("error")

def test_files():
    assert os.path.isfile(pipe.output),f'{output} is not a file.'
    assert os.path.isfile(pipe.output2),f'{output2} is not a file.'
    print("Assertion passed: output_file is a file.")

def test_datapipeline():
    pipe.worldbank_Data(pipe.output)
    pipe.HDR(pipe.output2)
    assert os.path.isfile(pipe.DATABASE_PATH), f'{pipe.DATABASE_PATH} is not a file'
    print(f"Assertion passed: {pipe.DATABASE_PATH} is a file.")
    conn = sqlite3.connect(pipe.DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' and name='worldbank';")
    worldbank = cur.fetchall()
    if len(worldbank)>=1:
        print('worldbank table exists')
    else:
        print('worldbank table does not exists')

    cur.execute("SELECT name FROM sqlite_master WHERE type='table' and name = 'HDR';")
    hdr = cur.fetchall()
    if len(hdr)>=1:
        print('HDR table exists')
    else:
        print('HDR table does not exists')
    conn.close()

'''
def test_worldbank_data():
    pipe.worldbank_Data(pipe.output)
    assert os.path.isfile(pipe.DATABASE_PATH), f'{pipe.DATABASE_PATH} is not a file'
    print(f"Assertion passed: {pipe.DATABASE_PATH} is a file.")

    conn = sqlite3.connect(pipe.DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' and name='worldbank';")
    worldbank = cur.fetchall()
    if len(worldbank)>=1:
        print('worldbank table exists')
    else:
        print('worldbank table does not exists')
    conn.close()

def test_HDR():
    pipe.HDR(pipe.output2)
    assert os.path.isfile(pipe.DATABASE_PATH), f'{pipe.DATABASE_PATH} is not a file'
    print(f"Assertion passed: {pipe.DATABASE_PATH} is a file.")

    conn = sqlite3.connect(pipe.DATABASE_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' and name = 'HDR';")
    hdr = cur.fetchall()
    if len(hdr)>=1:
        print('HDR table exists')
    else:
        print('HDR table does not exists')
    conn.close()
'''
test_get_request(pipe.url,pipe.output)
test_get_request(pipe.url2,pipe.output2)
test_files()
#test_worldbank_data()
#test_HDR()
test_datapipeline()
