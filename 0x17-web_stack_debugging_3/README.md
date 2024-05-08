# Puppet Automation for Apache Error Resolution

This repository contains a Puppet script (`0-strace_is_your_friend.pp`) designed to identify and resolve a `500 Internal Server Error` returned by an Apache server. By using `strace` to diagnose the problem and Puppet to apply the fix, this process is fully automated, enhancing reliability and ease of maintenance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed on your machine:

- Apache server (Preferably Apache/2.4.7 running on Ubuntu)

- Puppet
- `strace` utility
- `tmux` for session management
- `curl` for sending HTTP requests
