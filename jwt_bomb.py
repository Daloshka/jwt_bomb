from jose import jwt
import time

# Загрузка RSA ключей
with open('private_key.pem', 'r') as f:
    private_key = f.read()

with open('public_key.pem', 'r') as f:
    public_key = f.read()

# Большой payload
large_payload_length = 40000000
large_payload = '{"u": "' + "u" * large_payload_length + '", "uu":"' + "u" * large_payload_length + '"}'
print(f"Length of large payload: {len(large_payload)}")

# Подпись большого payload
v1 = jwt.encode({'data': large_payload}, private_key, algorithm='RS256')
print(f"Length of signed large payload: {len(v1)}")

# Сохранение большого JWT токена в файл
with open('large_token.txt', 'w') as f:
    f.write(v1)

# Измерение времени проверки подписи для большого payload
begin = time.time()
jwt.decode(v1, public_key, algorithms=['RS256'])
print(f"Verification time for large payload: {time.time() - begin} seconds")

# Маленький payload
small_payload_length = 40000
small_payload = '{"u": "' + "u" * small_payload_length + '", "uu":"' + "u" * small_payload_length + '"}'
print(f"Length of small payload: {len(small_payload)}")

# Подпись маленького payload
v2 = jwt.encode({'data': small_payload}, private_key, algorithm='RS256')
print(f"Length of signed small payload: {len(v2)}")

# Сохранение маленького JWT токена в файл
with open('small_token.txt', 'w') as f:
    f.write(v2)

# Измерение времени проверки подписи для маленького payload
begin = time.time()
jwt.decode(v2, public_key, algorithms=['RS256'])
print(f"Verification time for small payload: {time.time() - begin} seconds")
