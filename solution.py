class FileReader():

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            f = open(self.file_path)
            text = f.read()
            f.close()
            return str(text)
        except FileNotFoundError:
            return ""