#!/usr/bin/env bash
#Puppet client congiguration

file {"etc/ssh/ssh_config":
	ensure => present,
content =>"
	#Client ssh config
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
",
}
