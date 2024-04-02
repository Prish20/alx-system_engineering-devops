#!/usr/bin/env bash
#Puppet client congiguration

package { 'openssh-client':
  ensure => installed,
}

file {'ect/ssh/ssh_config':
	ensure => present,
	content =>"
	#Client ssh config
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
