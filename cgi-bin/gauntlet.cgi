#!/usr/bin/perl -T

# This file is part of retro-gauntlet.
# 
# retro-gauntlet is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# retro-gauntlet is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with retro-gauntlet.  If not, see <http://www.gnu.org/licenses/>.

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
