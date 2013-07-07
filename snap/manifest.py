def run(self):

    print(self.get_nodes(["testy"]))
    print(self.get_nodes_in_group("front_end_nodes"))

    self.local_script("test1")
    self.stage('.',['foo'],['bar'])
    self.remote_script("test2")
