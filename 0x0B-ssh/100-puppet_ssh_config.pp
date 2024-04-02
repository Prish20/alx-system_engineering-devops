#!/usr/bin/env bash
# Using puppet to make changes to the SSH config file

file {'etc/ssh/ssh_config':
    ensure => present,
content => "
# This is the ssh client system-wide configuration file.
# See ssh_config(5) for more information. This file provides defaults for
# users, and the values can be changed in per-user configuration files
# or on the command line.
    host*
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
