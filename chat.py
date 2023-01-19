from interface import *


class Chatroom():

    def on_closing(self):
        self.root.destroy()
        self.app.disconnect_from_server()

    def run(self, user):
        self.root = Tk()
        self.root.title("PROTON++")
        self.root.geometry(default_window_size)
        self.root.minsize(360, 200)

        # start application
        self.app = ChatInterface(self.root, fullname=user)
        self.app.default_format()

        # root is your root window
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.root.mainloop()
