#fileName:arithmetic.py

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("Today:", now.toString(Qt.ISODate))
print("Adding 12 days:{0}".format(now.addDays(12).toString(Qt.ISODate)))
print("Subtracting 22 days:{0}".format(now.addDays(-22).toString(Qt.ISODate)))

print("Adding 50 seconds:{0}".format(now.addSecs(50).toString(Qt.ISODate)))
print("Adding 3 seconds:{0}".format(now.addSecs(3).toString(Qt.ISODate)))
print("Adding 12 seconds:{0}".format(now.addSecs(12).toString(Qt.ISODate)))