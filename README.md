webmin-bloctweet
================

![Bloctweet Webmin module screenshot](http://i.imgur.com/mZ58Env.png)

Bloctweet Group Tweet Server configuration module. Bloctweet is a simple server, written by Corey Williams, to facilitate groups who wish to tweet on a single account. It can be used by companies, organizations, activists, and other groups to share a Twitter account without sharing the password amongst the users. It has no fixed limits on number of contributors.

This is a Webmin module to edit the configuration file for Bloctweet. It currently does not start, stop,
or otherwise manage the server but supports all editable configuraton options, including contributors.

To install, download the .wbm package from http://austinlinuxguy.com/files/bloctweet-1.0.wbm.gz , and use Webmin's Webmin Modules page (Webmin->Webmin Configuration->Webmin Modules). You'll need the Perl Config::INI module from CPAN. This module is widely available for OS repos (and EPEL for CentOS/RHEL), so it can be installed with apt-get or yum.

If developing on the module, you can clone the git repo into your Webmin directory (/usr/libexec/webmin on RHEL and Fedora based systems, /usr/share/webmin on Debian and Ubuntu based systems, /usr/local/webmin on other systems), copy config into /etc/webmin/bloctweet, and delete your module.infos.cache.
