#puppet manifest that sets up your web servers for the deployment of web_static

$str = "add_header X-Served-By ${hostname};"
$hbnb_static = "\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tindex index.html index.htm;\n\t}"

exec { 'update':
  command  => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

-> exec { 'mkdir':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => 'shell'
}

-> exec { 'mkdir_2':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => 'shell',
}

-> exec { 'link':
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => 'shell',
}

-> exec { 'ownership':
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  provider => 'shell',
}

-> file_line { '301 Moved Permanently':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=0MW0mDZysxc permanent;',
}

-> file_line { 'X-Served-By':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => $str,
}

-> file_line { 'alias':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'index  index.html index.htm;',
  line   => $hbnb_static,
}

-> exec { 'Holberton School':
  command  => 'sudo echo "Holberton School" | sudo tee /usr/share/nginx/html/index.html',
  provider => 'shell',
}

-> service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
