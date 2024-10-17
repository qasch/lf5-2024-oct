# Dateizugriff 

# Dateipfade / Pfadangaben
# absolute Pfadangaben    egal wo wir uns befinden -> C:\User\Peter\Documents
# relative Pfadangaben    wir befinden uns in:[C:\User] ->  Peter\Documents
#   pfad/zur/datei
#   ./pfad/zur/datei     # ein einzelner Punkt . steht für das aktuelle Verzeichnis
#   ../pfad/zur/datei    # ein doppelter Punkt .. steht für das übergeordente Verzeichnis

#file = open("/home/kschell/code/LF5-202410/code/testfile.txt", "r")   # Angabe des absoluten Pfades zur Datei
# C:Benutzerkschellcode\testfile.txt
# Datei bearbeiten - lesen/schreiben
# unter Windows:
# C:/Benutzer/kschell/code/testfile.txt    
# C:\\Benutzer\\kschell\\code\\testfile.txt    
# -> C:\Benutzer\kschell\code\testfile.txt    
# pfade = r"C:\Benutzer\kschell\code\testfile.txt"   # Raw String    

# Datei öffnen - Zugriff über Stream
try:
    file = open("testfile.txt", "r")   # Angabe des relativen Pfades zur Datei
    text = file.read()
    print(text)

    # Stream schliessen
    file.close()
except TypeError as t:
    print("(TypeError) Folgender Fehler ist aufgetreten:", t.args[1])
except IOError as i:
    print("(IOError) Folgender Fehler ist aufgetreten:", i.args[1])
except FileNotFoundError as f:
    print("(FileNotFoundError) Folgender Fehler ist aufgetreten:", f.args[1])
except:
    print("(Exception) Ein unbekannter Fehler ist aufgetreten.")


print("Nach der Exception läuft unser Programm weiter!")
