import logging

# debug
# info
# warning
# error
# critical

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
logging.debug("This is a debug error")
logging.info("This is a info error")
logging.warning("This is a warning error")
logging.error("This is a error error")
logging.critical("This is a critical error")

a = int(input("Enter value: "))
b = int(input("Enter value: "))

try:
    c = a / b
    print("output is ", c)
except Exception as e:
    logging.error("exception happened", exc_info=True)

