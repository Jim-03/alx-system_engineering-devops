# Create a file at /tmp/school with specified permissions, owner, group, and content
file { 'school':
  ensure  => 'file',         # Ensure the resource is a file
  path    => '/tmp/school',  # File path
  mode    => '0744',         # File permissions
  owner   => 'www-data',     # File owner
  group   => 'www-data',     # File group
  content => 'I love Puppet',# Content inside the file
}
