# install_check.pl

do 'bloctweet-lib.pl';

# is_installed(mode)
# For mode 1, returns 2 if the server is installed and configured for use by
# Webmin, 1 if installed but not configured, or 0 otherwise.
# For mode 0, returns 1 if installed, 0 if not
sub is_installed
{
# Available config file in the default location?
return 0 if (!-x $config{'bloctweet_config'});
return 1;
}

