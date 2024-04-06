package { 'python3':
  ensure => 'installed',
}

exec { 'install_pip3':
  command => '/usr/bin/apt-get -y install python3-pip',
  unless  => '/usr/bin/dpkg -l python3-pip',
  require => Package['python3'],
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  environment => ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  unless      => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require     => Exec['install_pip3'],
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}

