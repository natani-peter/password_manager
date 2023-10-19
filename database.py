#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}
                                                                                                                                e username='john'")
# # users =cursor.fetchall()
# # # cursor.execute("delete from users")
# # # connection.commit()
# # # print(users[0][0])
# #
# # cursor.execute("select * from passwords")
# # results = cursor.fetchall()
# # name = input("username:\t")
# # one = cursor.execute("select user_id from users where username = ?",(name,))
# # id = one.fetchone()[0]
# # two = cursor.execute("select app,password from passwords where user_id = ?",(id,))
# # passwords = two.fetchall()
# # for password in passwords:
# #     print(password)
# # name = input('username:\t')
# # email = name+"@gmail.com"
# # password = input("password:\t") # 12345
# # salt = bcrypt.gensalt()
# # hashed = bcrypt.hashpw(password.encode(),salt)
# # cursor.execute("insert into users (username,email,password) values (?,?,?)",(name,email,hashed))
# connection.commit()
# # password = str(1234)
# # cursor.execute("select password from users where username = 'peter'")
# # stored = cursor.fetchone()
# # prove = bcrypt.checkpw(password.encode(),stored[0])
# # print(prove)
#
# connection.close()
#
#
import sqlite3
import customtkinter as ctk
import tkinter as tk

class Query(ctk.CTk):
    def __init__(self):
        super(Query, self).__init__()
        self.title('DATAQUERY')
        self.geometry("500x300")
        self.resizable(False,False)
        connection = sqlite3.connect('words.db')
        self.cursor = connection.cursor()

        self.search = ctk.CTkEntry(self)
        self.search.pack(fill='x',padx=40,pady=10)

        self.listview = tk.Listbox(self)
        self.listview.pack(expand=True,fill='both',pady=10,padx=10)

        self.display()

        self.bind("<KeyRelease>", self.updatewindow)
        self.mainloop()
        connection.close()

    def display(self):
        self.cursor.execute("select * from words")
        values = self.cursor.fetchall()
        self.listview.delete(0, tk.END)
        for result in values:
            self.listview.insert(tk.END, result)

    def updatewindow(self,event):
        query = ""
        query = self.search.get()
        self.cursor.execute("select * from words where words like ? ",("%" + query + "%",))
        results = self.cursor.fetchall()
        self.listview.delete(0,tk.END)
        for result in results:
            self.listview.insert(tk.END, result)


Query()