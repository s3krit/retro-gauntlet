#!/usr/bin/perl -T
use strict;
use CGI;
srand;
my $q = CGI->new;
my $system = $q->param('system');
my $game;
$system =~ s/([a-z0-9]+)/$1/g;
$system = $1;

open FILE, "./systems/".$system or seterr($!) and die;
rand($.)<1 and ($game=$_) while <FILE>;
close FILE;
$game =~ s/ $//;
$game =~ s/[\n\r]//g;
my $body = "<h1>Your game is \"$game\"! Now go play it</h1>";
printout($body);

sub printout{
print <<EOF;
Content-type: text/html; charset=utf-8\n\n
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Retro Game Gauntlet</title>
<link rel="stylesheet" type="text/css" href="../style.css" />
<link href='http://fonts.googleapis.com/css?family=Press+Start+2P' rel='stylesheet' type='text/css'>
</head>
<body>
$_[0]
</body>
</html>
EOF
}

sub seterr{
	my $errmsg = "<h1>Error!</h1><p>$_[0]</p>";
	printout($errmsg);
}
