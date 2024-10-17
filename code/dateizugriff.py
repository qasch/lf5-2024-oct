# Dateizugriff 

# Dateipfade / Pfadangaben
# absolute Pfadangaben    egal wo wir uns befinden -> C:\User\Peter\Documents
# relative Pfadangaben    wir befinden uns in:[C:\User] ->  Peter\Documents


# Datei öffnen - Zugriff über Stream
file = open("/home/kschell/code/LF5-202410/code/testfile.txt", "r")   # Angabe des Pfades zur Datei

# Datei bearbeiten - lesen/schreiben
text = file.read()
print(text)

# Stream schliessen
file.close()