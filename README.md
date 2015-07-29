[![Circle CI](https://circleci.com/gh/rackspace-orchestration-templates/lamp/tree/master.png?style=shield)](https://circleci.com/gh/rackspace-orchestration-templates/lamp)
Description
===========

This is a template for deploying a LAMP stack on a single Linux server. This
template is leveraging [ansible](http://www.ansible.com/home) with a
[chef-solo](http://docs.opscode.com/chef_solo.html) wrapper to setup the
server.

Requirements
============
* A Heat provider that supports the Rackspace `OS::Heat::ChefSolo` plugin.
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Example Usage
=============
Here is an example of how to deploy this template using the
[python-heatclient](https://github.com/openstack/python-heatclient):

```
heat --os-username <OS-USERNAME> --os-password <OS-PASSWORD> --os-tenant-id \
  <TENANT-ID> --os-auth-url https://identity.api.rackspacecloud.com/v2.0/ \
  stack-create LAMP-Stack -f lamp.yaml -P flavor="4 GB Performance"
```

* For UK customers, use `https://lon.identity.api.rackspacecloud.com/v2.0/` as
the `--os-auth-url`.

Optionally, set environmental variables to avoid needing to provide these
values every time a call is made:

```
export OS_USERNAME=<USERNAME>
export OS_PASSWORD=<PASSWORD>
export OS_TENANT_ID=<TENANT-ID>
export OS_AUTH_URL=<AUTH-URL>
```

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `server_hostname`: Sets the hostname of the server. (Default: web)
* `image`: Operating system to install (Default: CentOS 6.5 (PVHVM))
* `flavor`: Cloud server size to use. (Default: 1 GB Performance)
* `phpmyadmin_user`: User name for the first factor of logging into phpMyAdmin.
  (Default: serverinfo)
* `kitchen`: URL for the kitchen to clone with git. The Chef Solo run will copy
  all files in this repo into the kitchen for the chef run. (Default:
  https://github.com/rillip3/ChefAnsibleWrapper/)
* `chef_version`: Chef client version to install for the chef run. (Default:
  11.12.8)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value fo a specific output.

* `private_key`: SSH private that can be used to login as root to the server.
* `server_ip`: Public IP address of the cloud server
* `phpmyadmin_url`: URL to the phpMyAdmin installation.
* `phpmyadmin_user`: Username for the first factor of authentication for
  phpMyAdmin
* `phpmyadmin_password`: Password for the first factor of authentication for
  phpMyAdmin
* `mysql_root_password`: MySQL Root Password

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.

Stack Details
=============
#### Getting Started
This deployment is intended for small workloads, such as a site in
development. For a larger work load, consider using the PHP Application
Deployment instead, as it will provide a much better setup for scaling
production workloads.

#### What is provided
This deployment configures a Cloud Server running Apache, MySQL, PHP, and
phpMyAdmin. A simple firewall rule set is configured allowing access to
Apache and SSH.

#### Logging in via SSH
The private key provided in the passwords section can be used to login as
root via SSH.  We have an article on how to use these keys with [Mac OS X and
Linux](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-linuxmac)
as well as [Windows using
PuTTY](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-windows).

#### Details of Your Setup
[Apache](http://www.apache.org/) v2.2 is installed on Red Hat Enterprise
Linux 6, CentOS 6, Debian 7, Ubuntu 10.04 and 12.04. Ubuntu 14.04 and CentOS 7
come with Apache 2.4.

[MySQL](http://www.mysql.com/) v5.1 is installed on Ubuntu 10.04. MySQL v5.5
is installed on Ubuntu 12.04, 14.04, Redhat Enterprise Linux 6 and CentOS 6.
[MariaDB](https://mariadb.com/) is the default on CentOS 7.

The MySQL root password is recorded in root's home directory in the
file .my.cnf and in the View Generated Passwords dialog. Daily database
backups are taken using [Holland](http://hollandbackup.org/). A rotating
seven days of database dumps are stored in /var/lib/mysqlbackup.

[PHP](http://www.php.net/) is installed at v5.3 on Ubuntu 12.04, v5.4 on
Redhat Enterprise Linux 6, CentOS 6 and Debian 7, v5.5 on Ubuntu 14.04,
and v5.6 on CentOS 7,

[phpMyAdmin](http://www.phpmyadmin.net/) is available via HTTP at
/phpmyadmin. Apache is configured to require HTTP basic authentication. Log
in as the user specified when deploying (the default is `admin`) with the
password displayed in the View Generated Passwords dialog. You may then login
using MySQL login credentials which are also available in the View Generated
Passwords dialog.

Contributing
============
There are substantial changes still happening within the [OpenStack
Heat](https://wiki.openstack.org/wiki/Heat) project. Template contribution
guidelines will be drafted in the near future.

License
=======
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
