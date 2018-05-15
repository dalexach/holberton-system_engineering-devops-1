# Fixes an error with a WordPress Website
exec { 'replace':
  onlyif  => 'test -e /var/www/html/wp-includes/class-wp-locale.php',
  command => "sed -i 's/phpp/php/' /var/www/html/wp-includes/class-wp-locale.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
