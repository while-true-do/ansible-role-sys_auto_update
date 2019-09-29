<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-sys_auto_update.svg)](https://github.com/while-true-do/ansible-role-sys_auto_update/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-sys_auto_update.svg)](https://github.com/while-true-do/ansible-role-sys_auto_update/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-sys_auto_update.svg)](https://github.com/while-true-do/ansible-role-sys_auto_update/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-sys_auto_update.svg)](https://github.com/while-true-do/ansible-role-sys_auto_update/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-sys_auto_update.svg)](https://travis-ci.com/while-true-do/ansible-role-sys_auto_update)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_auto_update%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_auto_update)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_auto_update%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_auto_update)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_auto_update%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_auto_update)

# Ansible Role: sys_auto_update

An Ansible Role to install and configure automatic updates on various linux
distributions.

## Motivation

Doing updates on multiple machines is critical, but time consuming. Having a
service, which is taking care of automatic updates from time to time reduces
the effort for maintenance. Automatic updates can be applied to small home
machines and with some minor tuning to productive enterprise machines, too.

You should also have a patching / maintenance plan to due stuff like upgrades,
checking various security settings and do reboots.

## Description

This Ansible Role installs and configures automatic updates:

- install and configure needed packages (yum-cron, dnf-automatic)
- configure the services properly
- start the services or timers

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible Template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/sys_auto_update)
```
ansible-galaxy install while_true_do.sys_auto_update
```

Install from [Github](https://github.com/while-true-do/ansible-role-sys_auto_update)
```
git clone https://github.com/while-true-do/ansible-role-sys_auto_update.git while_true_do.sys_auto_update
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.sys_auto_update

## Package Management
# Defaults are based on Fedora Linux
wtd_sys_auto_update_package: "dnf-automatic"
# State can be present|latest|absent
wtd_sys_auto_update_package_state: "present"

## Configuration Management
wtd_sys_auto_update_conf_cmd:
  # Can be default|security, depending on your distribution
  update_type: "default"
  download_updates: "yes"
  apply_updates: "yes"
  random_sleep: 360

wtd_sys_auto_update_conf_notify:
  # unset = use hostname
  system_name: ""
  # can be stdio|mail
  notify_via: "stdio"
  email_from: "root@localhost"
  email_to: "root"
  email_host: "localhost"

## Service Management
wtd_sys_auto_update_service: "dnf-automatic"
# State can be started|stopped
wtd_sys_auto_update_service_state: "started"
wtd_sys_auto_update_service_enabled: true
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.sys_auto_update
```

#### Advanced

Apply security updates and send notifications via e-mail.

```
- hosts: all
  roles:
    - role: while_true_do.sys_auto_update
    wtd_sys_auto_update_conf_cmd:
      update_type: "security"

    wtd_sys_auto_update_conf_notify:
      notify_via: "mail"
      email_to: "mail@example.com"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-sys_auto_update/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-sys_auto_update/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
