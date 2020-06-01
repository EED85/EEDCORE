import pkg_resources
import pandas as pd
df = pd.read_json(r"C:\DEV\git\EED85\EED-CORE\src\python_environment\data\packages_37.json",orient='table')

class PythonEnvironmentHandler(object):
    def init(self):
        #class attributes
        self.l_pkg_na_gha = ['menuinst','mkl-service==2.3.0' ,'conda==4.8.3']
        self.requirements_file = "requirements.txt"
    def create_requirements(self,usage):
        if usage == "pip":
            pass
        elif usage == "conda":
        elif usage == "ghe":
            for pckg in :
                if pckg not in self.l_pkg_na_gha:
                    print(pckg.project_name + "==" + pckg.version)
    def get_os():
        pass
    def print_pakgackes(self):
        [print(d.project_name + "==" + d.version) for d in pkg_resources.working_set]

