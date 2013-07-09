def run(self):

    self.tag("wut-it-do")

    fens = self.get_nodes_in_group("front_end_nodes")

    self.local_script("test1")
    self.stage('.',['foo'],['bar'],fens)
    self.remote_script("test2",fens)
