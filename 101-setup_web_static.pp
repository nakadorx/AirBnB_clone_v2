#puppet manifest that sets up your web servers for the deployment of web_static

$def = 'server {
	listen 80;
	listen [::]:80 default_server;
	root   /usr/share/nginx/html;
	index  index.html index.htm;
    add_header X-Served-By $HOSTNAME;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
		return 301 http://youtube.com/;
	}

	error_page 404 /notfound.html;
	location = /notfound {
		root /usr/share/nginx/html;
		internal;
	}
}'

exec { 'update':
  command  => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

-> file { '/data/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}
-> file { '/data/web_static/releases':
    ensure => 'directory',
}

-> file { '/data/web_static/releases/test':
    ensure => 'directory',
}

-> file { '/data/web_static/shared/':
    ensure => 'directory',
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Holberton School',
}

-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
}

-> file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $def,
}

-> service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
