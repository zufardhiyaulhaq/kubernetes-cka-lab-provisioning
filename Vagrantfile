# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.box = 'hashicorp/bionic64'

  # k8s-cluster
  config.vm.define 'k8s-master' do |master|
    master.vm.hostname = 'k8s-master'
    master.vm.network 'private_network', ip: '10.200.200.100'
    master.vm.provider 'virtualbox' do |vb|
      vb.name = 'k8s-master'
      vb.memory = 4000
      vb.cpus = 2
    end
  end

  (1..2).each do |i|
    config.vm.define "k8s-worker#{i}" do |worker|
      worker.vm.hostname = "k8s-worker#{i}"
      worker.vm.network 'private_network', ip: "10.200.200.10#{i}"
      worker.vm.provider 'virtualbox' do |vb|
        vb.name = "k8s-worker#{i}"
        vb.memory = 4000
        vb.cpus = 2
      end
    end
  end

  # hk8s-cluster
  config.vm.define 'hk8s-master' do |master|
    master.vm.hostname = 'hk8s-master'
    master.vm.network 'private_network', ip: '10.200.200.110'
    master.vm.provider 'virtualbox' do |vb|
      vb.name = 'hk8s-master'
      vb.memory = 2000
      vb.cpus = 2
    end
  end

  (1..2).each do |i|
    config.vm.define "hk8s-worker#{i}" do |worker|
      worker.vm.hostname = "hk8s-worker#{i}"
      worker.vm.network 'private_network', ip: "10.200.200.11#{i}"
      worker.vm.provider 'virtualbox' do |vb|
        vb.name = "hk8s-worker#{i}"
        vb.memory = 2000
        vb.cpus = 2
      end
    end
  end

  # bk8s-cluster
  config.vm.define 'bk8s-master' do |master|
    master.vm.hostname = 'bk8s-master'
    master.vm.network 'private_network', ip: '10.200.200.120'
    master.vm.provider 'virtualbox' do |vb|
      vb.name = 'bk8s-master'
      vb.memory = 2000
      vb.cpus = 2
    end
  end

  (1..1).each do |i|
    config.vm.define "bk8s-worker#{i}" do |worker|
      worker.vm.hostname = "bk8s-worker#{i}"
      worker.vm.network 'private_network', ip: "10.200.200.12#{i}"
      worker.vm.provider 'virtualbox' do |vb|
        vb.name = "bk8s-worker#{i}"
        vb.memory = 2000
        vb.cpus = 2
      end
    end
  end

  # wk8s-cluster
  config.vm.define 'wk8s-master' do |master|
    master.vm.hostname = 'wk8s-master'
    master.vm.network 'private_network', ip: '10.200.200.130'
    master.vm.provider 'virtualbox' do |vb|
      vb.name = 'wk8s-master'
      vb.memory = 2000
      vb.cpus = 2
    end
  end

  (1..2).each do |i|
    config.vm.define "wk8s-worker#{i}" do |worker|
      worker.vm.hostname = "wk8s-worker#{i}"
      worker.vm.network 'private_network', ip: "10.200.200.13#{i}"
      worker.vm.provider 'virtualbox' do |vb|
        vb.name = "wk8s-worker#{i}"
        vb.memory = 2000
        vb.cpus = 2
      end
    end
  end

  # ek8s-cluster
  config.vm.define 'ek8s-master' do |master|
    master.vm.hostname = 'ek8s-master'
    master.vm.network 'private_network', ip: '10.200.200.140'
    master.vm.provider 'virtualbox' do |vb|
      vb.name = 'ek8s-master'
      vb.memory = 2000
      vb.cpus = 2
    end
  end

  (1..2).each do |i|
    config.vm.define "ek8s-worker#{i}" do |worker|
      worker.vm.hostname = "ek8s-worker#{i}"
      worker.vm.network 'private_network', ip: "10.200.200.14#{i}"
      worker.vm.provider 'virtualbox' do |vb|
        vb.name = "ek8s-worker#{i}"
        vb.memory = 2000
        vb.cpus = 2
      end
    end
  end

  # ik8s-cluster
  config.vm.define 'ik8s-master' do |master|
    master.vm.hostname = 'ik8s-master'
    master.vm.network 'private_network', ip: '10.200.200.150'
    master.vm.provider 'virtualbox' do |vb|
      vb.name = 'ik8s-master'
      vb.memory = 2000
      vb.cpus = 2
    end
  end

  (1..1).each do |i|
    config.vm.define "ik8s-worker#{i}" do |worker|
      worker.vm.hostname = "ik8s-worker#{i}"
      worker.vm.network 'private_network', ip: "10.200.200.15#{i}"
      worker.vm.provider 'virtualbox' do |vb|
        vb.name = "ik8s-worker#{i}"
        vb.memory = 2000
        vb.cpus = 2
      end
    end
  end

  config.vm.provision 'deploy', type: 'ansible', run: 'never' do |ansible|
    ansible.groups = {
      'controllers' => %w[zu-ovn-controller-0],
      'computes' => %w[zu-ovn-compute-0 zu-ovn-compute-1 zu-ovn-compute-2]
    }
    ansible.playbook = 'provisioning/main.yml'
  end
end
