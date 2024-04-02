#!/usr/bin/perl
use strict;
use warnings;
use Getopt::Long;
use Opsware::NAS::Connect;

my($host, $port, $user, $pass) = ('localhost','$tc_proxy_telnet_port$','$tc_user_username$','$tc_user_password$');
my $device = '#$tc_device_id$';
my @output;

my $con = Opsware::NAS::Connect->new(-user => $user, -pass => $pass, -host => $host, -port => $port);

$con->login();
$con->connect( $device ) or die "Failed to connect.";

$con->cmd("terminal length 0");

    
print "show running-conf\n";
@output = $con->cmd("show running-conf");
print join("\n", @output);

    
print "show snmp group\n";
@output = $con->cmd("show snmp group");
print join("\n", @output);

    
print "show snmp user\n";
@output = $con->cmd("show snmp user");
print join("\n", @output);

    
print "show snmp engineID\n";
@output = $con->cmd("show snmp engineID");
print join("\n", @output);

    
print "show snmp user rttadmin\n";
@output = $con->cmd("show snmp user rttadmin");
print join("\n", @output);

    
@output = $con->disconnect();

$con->logout();
undef $con;
exit(0);