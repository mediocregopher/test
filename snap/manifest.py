def run(self):

    self.local_script("test1")
    self.stage('.',['foo'],['bar'])
    self.remote_script("test2")
