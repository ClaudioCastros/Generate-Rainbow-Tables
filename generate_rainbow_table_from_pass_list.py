import hashlib, sys
from datetime import datetime
'''  
str2hash = "GeeksforGeeks"
  
result_md5 = hashlib.md5(str2hash.encode())
result_sha1 = hashlib.sha1(str2hash.encode())
result_sha224 = hashlib.sha224(str2hash.encode())
result_sha256 = hashlib.sha256(str2hash.encode())
result_sha384 = hashlib.sha384(str2hash.encode())
  
print(result_md5.hexdigest())
print(result_sha1.hexdigest())
print(result_sha224.hexdigest())
print(result_sha256.hexdigest())
print(result_sha384.hexdigest())
'''

if len(sys.argv) > 2:
    print('\nERRO: Apenas o nome do arquivo contendo a lista de senhas deve ser passado como argumento.\n')
    exit()
elif len(sys.argv) == 1:
    print('\nINFO: Um arquivo contendo uma lista de senhas deve ser passado como parametro.\nexemplo: generate_rainbow_table_from_pass_list.py 1000-most-common-passwords.txt\n')
    exit()
else:

    print(
    '''
    \n
    1. MD5
    2. SHA-1
    3. SHA-224
    4. SHA-256
    5. SHA-384
    ''')
    hash_alg = int(input("Deseja gerar o Rainbow Table utilzando qual algoritmo de hash? "))

    while True:
        if hash_alg in [1,2,3,4,5]:
            break
        else:
            print("Valor não suportado.")
            hash_alg = input("Deseja gerar o Rainbow Table utilzando qual algoritmo de hash? ")

    list_of_rainbow = []

    file = sys.argv[1]
    try:
        # Using readlines()
        f = open(file, 'r')
        Lines = f.readlines()
        
        for line in Lines:

            line = line.replace("\n", "")

            if hash_alg == 1:
                result_md5 = hashlib.md5(line.encode())
                list_of_rainbow.append(f"{line}, {result_md5.hexdigest()}")

            elif hash_alg == 2:
                result_sha1 = hashlib.sha1(line.encode())
                list_of_rainbow.append(f"{line}, {result_sha1.hexdigest()}")

            elif hash_alg == 3:
                result_sha224 = hashlib.sha224(line.encode())
                list_of_rainbow.append(f"{line}, {result_sha224.hexdigest()}")

            elif hash_alg == 4:
                result_sha256 = hashlib.sha256(line.encode())
                list_of_rainbow.append(f"{line}, {result_sha256.hexdigest()}")

            elif hash_alg == 5:
                result_sha384 = hashlib.sha384(line.encode())
                list_of_rainbow.append(f"{line}, {result_sha384.hexdigest()}")

    except:
        print('Um erro ocorreu, não foi possivel processar o arquivo passado.')
        exit()

    n = {
        1: 'MD5',
        2: 'SHA-1',
        3: 'SHA-224',
        4: 'SHA-256',
        5: 'SHA-384'
    }
    

    dt = datetime.now()
    ts = datetime.timestamp(dt)

    with open(f'{ts}-generated-rainbow-table-{n[hash_alg]}.csv', 'w') as fp:
        for item in list_of_rainbow:
            
            fp.write(f"{item}\n")
        
        print('Done')
