#! /bin/bash

# Copyright (C) 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
#  
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

## Called as: initpost <cfgdir> <path of util-vserver-vars>

vdir=$1/vdir
cfgdir=$1
. "$2"

## Usage: subst <file> <regexp>
function subst
{
    tmp=$(mktemp /tmp/initpost-subst.XXXXXX)

    case "$1" in
	(/*|./*)	cat "$1";;
	(*)		$_CHROOT_SH cat "$1";;
    esac              | sed -e "$2"          >$tmp
    cmp -s $tmp "$1" || $_CHROOT_SH truncate "$1" <$tmp

    rm -f $tmp
}

pushd "$cfgdir" &>/dev/null
	# make convinient poldek.conf symlink
	ln -s apps/pkgmgmt/base/poldek/etc/poldek.conf poldek.conf
popd >/dev/null

pushd "$vdir" &>/dev/null
	if [ -f etc/sysconfig/rpm ]; then
		subst etc/sysconfig/rpm 's!^#RPM_SKIP_AUTO_RESTART=.*!RPM_SKIP_AUTO_RESTART=yes!'
	fi

	# for future. right now SysVinit is not created at build stage
	if [ -f etc/inittab ]; then
		# disable mingetty respawn
		subst etc/inittab 's!^\([^#].*:respawn:.* tty\)!#\1!'
	fi
popd >/dev/null
