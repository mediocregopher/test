import os
def run(self):

    print(self.get_chosen_destination_name_and_type())

    self.header(self.get_project_location())
    self.set_project_location(
        os.path.join(
            self.get_project_location(),
            "2"))
    self.header(self.get_project_location())

    self.stage('.')
