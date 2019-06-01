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

def tasks_generate():
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


if __name__ == "__main__":
    hosts_generate()
    tasks_generate()
