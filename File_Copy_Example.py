#copyfile() - Копира съдържанието в нов файл
#copy() - copyfile() + разрешения, дестинация може да е директория
#copy2 - copy() + всички метаданни, дата на създаване, модифицаране и т.н.

import shutil
shutil.copyfile("Test_File1.txt", "Test_File.txt")
print("Файла е копиран!")