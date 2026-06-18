import logging
logging.basicConfig(level=logging.DEBUG)
try:
    logging.info("Application started")
    userList = ["tree","car","train"]
    print(userList[7])
except Exception as e:
    logging.error(f"Error {e}")

print("this is the last line")