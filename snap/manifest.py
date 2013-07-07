def run(self):

    self.header("LOOK, A CHOICE")
    r = self.choice("the choice",
        {"A":"A","B":"B","C":"C"})
    self.header("YOU CHOSE {0}".format(r))

    self.local_script("test1")
    self.stage('.',['foo'],['bar'])
    self.remote_script("test2")
