# TODO: Edit the tests and remove this line.
# Some examples are given below.

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    file = host.file('/etc/hosts')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
