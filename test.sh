DEVICE_TYPE1=typ1
DEVICE_TYPE2=typ2
PORT=5000

# Adding devices
curl -X POST -H "Content-Type: application/json" localhost:${PORT}/devices -d "{ \"address\": \"addr1\", \"type\": \"${DEVICE_TYPE1}\", \"size\": 1000}"
curl -X POST -H "Content-Type: application/json" localhost:${PORT}/devices -d "{ \"address\": \"addr2\", \"type\": \"${DEVICE_TYPE2}\", \"size\": 500}"

# Pushing jobs
curl -X POST -H "Content-Type: application/json" localhost:${PORT}/jobs -d "{ \"priority\": 31, \"user_id\": \"uid1\", \"program_id\": \"prog11\",  \"device_type\": \"${DEVICE_TYPE2}\"}"
curl -X POST -H "Content-Type: application/json" localhost:${PORT}/jobs -d "{ \"priority\": 31, \"user_id\": \"uid2\", \"program_id\": \"prog22\",  \"device_type\": \"${DEVICE_TYPE1}\"}"
curl -X POST -H "Content-Type: application/json" localhost:${PORT}/jobs -d "{ \"priority\": 31, \"user_id\": \"uid2\", \"program_id\": \"prog22\",  \"device_type\": \"${DEVICE_TYPE1}\"}"
curl -X POST -H "Content-Type: application/json" localhost:${PORT}/jobs -d "{\"priority\": 31, \"user_id\": \"uid3\", \"program_id\": \"prog33\",  \"device_type\": \"${DEVICE_TYPE2}\"}"
