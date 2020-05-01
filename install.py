def hosts_generate():
    #Import necessary functions from Jinja2 module
    from jinja2 import Environment, FileSystemLoader

    #Import YAML module
    import yaml

    #Load data from YAML into Python dictionary
    config_data = yaml.load(open('./group_vars/all.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./hosts'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('hosts.j2')

    #Render the template with data and print the output
    with open("./hosts/hosts", "w") as fh:
        fh.write(template.render(config_data))

def main_tasks_generate():
    #Import necessary functions from Jinja2 module
    from jinja2 import Environment, FileSystemLoader

    #Import YAML & os module
    import yaml
    import os

    #Load data from YAML into Python dictionary
    config_data = yaml.load(open('./group_vars/all.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('main.yml.j2')

    #Render the template with data and print the output
    with open("main.yml", "w") as fh:
        fh.write(template.render(config_data))

    #delete "," in all line if exist
    os.system("sed -i 's/,$//' main.yml")

def master_setup_bootstraping():
    #Import necessary functions from Jinja2 module
    from jinja2 import Environment, FileSystemLoader

    #Import YAML module
    import yaml

    #Load data from YAML into Python dictionary
    config_data = yaml.load(open('./group_vars/all.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./roles/kubernetes-master-setup/tasks/'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('01-bootstraping.yml.j2')

    #Render the template with data and print the output
    with open("./roles/kubernetes-master-setup/tasks/01-bootstraping.yml", "w") as fh:
        fh.write(template.render(config_data))


def worker_setup_bootstraping():
    #Import necessary functions from Jinja2 module
    from jinja2 import Environment, FileSystemLoader

    #Import YAML module
    import yaml

    #Load data from YAML into Python dictionary
    config_data = yaml.load(open('./group_vars/all.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./roles/kubernetes-worker-setup/tasks/'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('01-bootstraping.yml.j2')

    #Render the template with data and print the output
    with open("./roles/kubernetes-worker-setup/tasks/01-bootstraping.yml", "w") as fh:
        fh.write(template.render(config_data))

def flannel():
    #Import necessary functions from Jinja2 module
    from jinja2 import Environment, FileSystemLoader

    #Import YAML module
    import yaml

    #Load data from YAML into Python dictionary
    config_data = yaml.load(open('./group_vars/all.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./roles/networking-flannel-setup/tasks/'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('flannel.yml.j2')

    #Render the template with data and print the output
    with open("./roles/networking-flannel-setup/tasks/flannel.yml", "w") as fh:
        fh.write(template.render(config_data))

def calico():
    #Import necessary functions from Jinja2 module
    from jinja2 import Environment, FileSystemLoader

    #Import YAML module
    import yaml

    #Load data from YAML into Python dictionary
    config_data = yaml.load(open('./group_vars/all.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./roles/networking-calico-setup/tasks/'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('calico.yml.j2')

    #Render the template with data and print the output
    with open("./roles/networking-calico-setup/tasks/calico.yml", "w") as fh:
        fh.write(template.render(config_data))

def deployer_kubeconfig():
    #Import necessary functions from Jinja2 module
    from jinja2 import Environment, FileSystemLoader

    #Import YAML module
    import yaml

    #Load data from YAML into Python dictionary
    config_data = yaml.load(open('./group_vars/all.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./roles/kubeconfig-deployer-setup/tasks/'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('01-copy.yml.j2')

    #Render the template with data and print the output
    with open("./roles/kubeconfig-deployer-setup/tasks/01-copy.yml", "w") as fh:
        fh.write(template.render(config_data))

def management_kubeconfig():
    #Import necessary functions from Jinja2 module
    from jinja2 import Environment, FileSystemLoader

    #Import YAML module
    import yaml

    #Load data from YAML into Python dictionary
    config_data = yaml.load(open('./group_vars/all.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./roles/kubeconfig-management-setup/tasks/'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('02-kubeconfig.yml.j2')

    #Render the template with data and print the output
    with open("./roles/kubeconfig-management-setup/tasks/02-kubeconfig.yml", "w") as fh:
        fh.write(template.render(config_data))

def initial_object():
    #Import necessary functions from Jinja2 module
    from jinja2 import Environment, FileSystemLoader

    #Import YAML module
    import yaml

    #Load data from YAML into Python dictionary
    config_data = yaml.load(open('./group_vars/all.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./initial-object'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('k8s-prepare-exam.j2')

    #Render the template with data and print the output
    with open("./initial-object/k8s-prepare-exam", "w") as fh:
        fh.write(template.render(config_data))

if __name__ == "__main__":
    hosts_generate()
    main_tasks_generate()
    master_setup_bootstraping()
    worker_setup_bootstraping()
    flannel()
    calico()
    deployer_kubeconfig()
    management_kubeconfig()
    initial_object()
