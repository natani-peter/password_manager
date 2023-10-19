#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi
                                            eturn>', self.give_focus)
        self.password.bind('<Return>', self.login)

        self.pack(expand=True, fill='both')

    def give_focus(self, event):
        self.password.focus_set()

    def login(self, event):
        username = self.username.get()
        password = self.password.get()

        cursor.execute('select * from users where username = ?', (username,))
        user = cursor.fetchone()
        if user:
            password_check = bcrypt.checkpw(password.encode(), user[-1])
            if password_check:
                self.pack_forget()
                HomeFrame(self.parent, username).pack(expand=True, fill='both')
                connection.close()
                self.password.unbind('<Return>')
            else:
                box.showerror(title='ERROR OCCURRED', message='Wrong Password')
        else:
            box.showerror(title='ERROR OCCURRED', message='User does not Exist!\n Consider creating an account!')

    def show(self):
        now = self.password.get()
        self.password = ctk.CTkEntry(self, placeholder_text='Password')
        self.password.grid(column=1, columnspan=3, row=3, sticky='ew')
        self.password.insert(0, now)
        ctk.CTkButton(self.password, 50, height=10, text='Hide', command=self.hide).place(relx=0.98, rely=0.5,
                                                                                          anchor='e')

    def hide(self):
        now = self.password.get()
        self.password = ctk.CTkEntry(self, placeholder_text='Password', show="*")
        self.password.grid(column=1, columnspan=3, row=3, sticky='ew')
        ctk.CTkButton(self.password, 50, height=10, text='show', command=self.show).place(relx=0.98, rely=0.5,
                                                                                          anchor='e')
        self.password.insert(0, now)

    def close(self):
        self.quit()
