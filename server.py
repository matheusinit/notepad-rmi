import os
import Pyro5.api


@Pyro5.api.expose
class Notepad(object):
    def write(self, message):
        file_exists = os.path.exists("notes.txt")

        if not file_exists:
            open("notes.txt", "a").close()

        file = open("notes.txt", "a")
        file.write(f"{message}\n")

        return "Message wrote."

    def read(self):
        file_exists = os.path.exists("notes.txt")

        if not file_exists:
            open("notes.txt", "a").close()

        file = open("notes.txt", "r")

        return file.read()


daemon = Pyro5.api.Daemon()
uri = daemon.register(Notepad)

print("Ready. Object uri =", uri)
daemon.requestLoop()
