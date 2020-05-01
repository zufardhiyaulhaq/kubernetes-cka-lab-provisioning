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

  # management
  config.vm.define 'management' do |management|
    management.vm.hostname = 'management'
    management.vm.network 'private_network', ip: '10.200.200.160'
    management.vm.provider 'virtualbox' do |vb|
      vb.name = 'management'
      vb.memory = 2000
      vb.cpus = 2
    end
  end

  config.vm.provision 'deploy', type: 'ansible', run: 'never' do |ansible|
    ansible.groups = {
      'k8s:children' => %w[k8smaster k8sworker],
      'k8smaster' => %w[k8s-master],
      'k8sworker' => %w[k8s-worker1 k8s-worker2],
      'hk8s:children' => %w[hk8smaster hk8sworker],
      'hk8smaster' => %w[hk8s-master],
      'hk8sworker' => %w[hk8s-worker1 hk8s-worker2],
      'bk8s:children' => %w[bk8smaster bk8sworker],
      'bk8smaster' => %w[bk8s-master],
      'bk8sworker' => %w[bk8s-worker1],
      'wk8s:children' => %w[wk8smaster wk8sworker],
      'wk8smaster' => %w[wk8s-master],
      'wk8sworker' => %w[wk8s-worker1 wk8s-worker2],
      'ek8s:children' => %w[ek8smaster ek8sworker],
      'ek8smaster' => %w[ek8s-master],
      'ek8sworker' => %w[ek8s-worker1 ek8s-worker2],
      'ik8s:children' => %w[ik8smaster ik8sworker],
      'ik8smaster' => %w[ik8s-master],
      'ik8sworker' => %w[ik8s-worker1],
      'management' => %w[ik8s-worker1]
    }
    ansible.playbook = 'main.yml'
  end
end
