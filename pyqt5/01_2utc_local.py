#fileName: utc_local.py

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("Local dateTime:", now.toString(Qt.ISODate))
print("Universal datetime:", now.toUTC().toString(Qt.ISODate))

print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc()))