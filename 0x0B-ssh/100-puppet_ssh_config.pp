#!/usr/bin/env bash
#Puppet client congiguration

file {'etc/ssh/ssh_config':
	ensure => present,
	content =>"
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}