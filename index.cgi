#!/usr/bin/perl

use warnings;
use strict;

our %text;

require 'bloctweet-lib.pl';

ui_print_header(undef, $text{'index_title'}, "", "index", 1, 1, 0,
    undef, undef, undef, undef);

my $bloctweet_config = get_bloctweet_config();

print ui_form_start('save_config.cgi', 'post');

# Settings section
print ui_hidden_table_start($text{'index_settings'}, "width=100%", 2, "settings", 1);

print ui_table_row($text{'index_settings_dm_enabled'},
	ui_yesno_radio('settings_dm_enabled',
	$bloctweet_config->{'settings'}{'dm_enabled'}, 1, 0), 1);

print ui_table_row($text{'index_settings_dm_refresh_rate'},
	ui_textbox('settings_dm_refresh_rate', $bloctweet_config->{'settings'}{'dm_refresh_rate'},
	'8'), 1);

print ui_table_row($text{'index_settings_hashtag_enabled'},
	ui_yesno_radio('settings_hashtag_enabled',
	$bloctweet_config->{'settings'}{'hashtag_enabled'}, 1, 0), 1);

print ui_table_row($text{'index_settings_search_hash'},
	ui_textbox('settings_search_hash', $bloctweet_config->{'settings'}{'search_hash'},
	'42'), 1);

print ui_table_row($text{'index_settings_refresh_rate'},
	ui_textbox('settings_refresh_rate', $bloctweet_config->{'settings'}{'refresh_rate'},
	'8'), 1);

print ui_table_row($text{'index_settings_account_name'},
	ui_textbox('settings_account_name', $bloctweet_config->{'settings'}{'account_name'},
	'42'), 1);

print ui_hidden_table_end();

# Contributors
print ui_hidden_table_start($text{'index_contributors'}, "width=100%", 2, "configuration", 1);

my $contributor_names;
foreach my $name (keys $bloctweet_config->{'contributors'}) {
	$contributor_names .= "$name\n";
}
print ui_table_row($text{'index_contributors'},
	ui_textarea('contributors', $contributor_names, 10, 42, 'off'), 1);

print ui_hidden_table_end();

# Keys section
print ui_hidden_table_start($text{'index_keys'}, "width=100%", 2, "keys", 0);

print ui_table_row($text{'index_keys_consumer_secret'},
	ui_textbox('keys_consumer_secret', $bloctweet_config->{'keys'}{'consumer_secret'}, '42'),
	1);

print ui_table_row($text{'index_keys_consumer_key'},
	ui_textbox('keys_consumer_key', $bloctweet_config->{'keys'}{'consumer_key'}, '42'), 
	1);

print ui_table_row($text{'index_keys_access_token'},
	ui_textbox('keys_access_token', $bloctweet_config->{'keys'}{'access_token'}, '42'), 
	1);

print ui_table_row($text{'index_keys_access_token_secret'},
	ui_textbox('keys_access_token_secret', $bloctweet_config->{'keys'}{'access_token_secret'}, '42'), 
	1);

print ui_hidden_table_end();

print ui_form_end([ [ "save", $text{'form_save'} ] ]); # save_config

ui_print_footer("/", $text{'index'});
