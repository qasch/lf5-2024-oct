# Exceptions 
#  - weder Syntax noch Logikfehler
#  - können(!) zur Laufzeit auftreten, müssen aber nicht
#  - wir haben keine Möglichkeit, diese zu vermeiden


try:
    # Code der ausgeführt werden soll
    # wir wissen, dass es zu einer Exception kommen kann
except:
    # falls es zu einer Exception kommt, führe diesen Block aus
    # in der Regel eine Fehlermeldung
    # das Programm stürzt aber nicht ab!
else:
    # wird nur ausgeführt, wenn es zu keiner Exception gekommen ist
finally:
    # wird immer ausgeführt, egal ob Exception oder nicht