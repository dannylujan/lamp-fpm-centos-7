# coding: utf-8
#
# Cookbook Name:: apache-prep
# Recipe:: default
#
# Copyright 2014
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# setup stock firewall rules
case node[:platform]
  when "debian", "ubuntu"
    package "python-apt"
    package "python-pip"
    package "build-essential"
    package "python-dev"
  when "redhat", "centos"
    package "python-pip"
end

execute "Install Ansible" do
  command "pip install paramiko PyYAML jinja2 httplib2 ansible"
  action :run
end

execute "sshkey" do
  command "`which ssh-keygen` -t rsa -f /root/.ssh/id_rsa -P '' -C ''"
  not_if "test -f /root/.ssh/id_rsa"
  action :run
end

cookbook_file "/root/.ansible.cfg" do
    source "ansible.cfg"
    owner "root"
    group "root"
    mode 0644
end

remote_directory "/root/lamp" do
  owner "root"
  group "root"
  mode 0755
  action :create
end

execute "ansible" do
  command "`which ansible-playbook` -i /root/lamp/hosts /root/lamp/site.yml -e 'mysql_password=#{node[:mysql][:server_root_password]} htuser=#{node[:phpmyadmin][:user]} htpass=#{node[:phpmyadmin][:pass]}'"
  action :run
end
