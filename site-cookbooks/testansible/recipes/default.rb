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
package "ansible" do
    options('--assumeyes')
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

remote_directory "/root/mcdev" do
  owner "root"
  group "root"
  mode 0755
  action :create
end

execute "ansible" do
  command "`which ansible-playbook` -vvv -i /root/mcdev/hosts /root/mcdev/site.yml"
  action :run
end
