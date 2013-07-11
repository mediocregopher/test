def run(self):

    fens = self.get_nodes_in_group("front_end_nodes")

    self.local_script("test1")

    yn = self.choice("Snap to fens?",False)
    if yn:
        self.stage('.',['foo'],['bar'],fens)
        self.remote_script("test2",fens)
