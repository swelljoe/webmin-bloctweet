#!/usr/bin/perl 

use strict;
use warnings;
use Error qw(:try);

our %config;

=head1 bloctweet-lib.pl

Functionsfor the bloctweet group tweet daemon module.

  foreign_require("bloctweet", "bloctweet-lib.pl");
  @tweet_schedule = bloctweet::list_schedule();

=cut

BEGIN { push(@INC, ".."); };
use WebminCore;
init_config();

=head2 get_bloctweet_config()

Returns the bloctweet configuration as a list of hash references with name an key value keys.

=cut

sub get_bloctweet_config {
	use Config::INI::Reader;

	my $config = Config::INI::Reader->read_file($config{'bloctweet_config'});
	return $config;
}

=head2 write_bloctweet_config(\%bloctweet_config)

Write configuration file array to config file. May return an error object, if write fails.

=cut

sub write_bloctweet_config {
	use Config::INI::Writer;
	my ($bloctweet_config) = @_;
	Config::INI::Writer->write_file($bloctweet_config, $config{'bloctweet_config'});
	return;
}

1;
