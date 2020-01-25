import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file, content', [
  ('/home/mary/.vimrc',
   'syntax on')
])
def test_files(host, file, content):
    f = host.file(file)

    assert f.exists
    assert f.contains(content)
    assert f.user == 'mary'
