## DESCRIPTION:

Complete LAMP configuration. This playbook will install a full Managed Operations based LAMP stack.

## REQUIREMENTS:

Ansible 1.6

## USAGE:

This playbook can be called with defaults or by role using "tags".

| Name | Examples
| ---------- | -------- |
| Full LAMP stack | ansible-playbook -i hosts site.yml
| MySQL server and Holland | ansible-playbook -i hosts site.yml -t mysql,holland
| Apache2 and PHP5 | ansible-playbook -i hosts site.yml -t apache2,php5

A full tag list can be found in the site.yml file


## LICENSE & AUTHOR:

Original Author: **Phil Eatherington**
Ansible Author: **Rocco Muscaritolo**
Ansible Author: **Johnny Martin**

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
