Exec {
  path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
}

group { "puppet":
    ensure => "present",
}

package { "git-core":
    ensure => "latest"
}

class { "webapp::python": owner => "vagrant",
                          group => "vagrant",
                          src_root => "/vagrant/apps",
                          venv_root => "/usr/local/venv",
}
webapp::python::instance { "project":
  domain => "project.iknuth.com",
  django => true,
}

