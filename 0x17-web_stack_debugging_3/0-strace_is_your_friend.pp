# Fixes an error with a WordPress Website
exec { 'replace':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-includes/class-wp-locale.php",
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  onlyif  => 'test -e /var/www/html/wwp-includes/class-wp-locale.php'
}
