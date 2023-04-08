#!/bin/bash
dir
=
"$HOME/.archive/" 
if [ -d $dir ]; then 
file
=
"$1"
null
=
""
else mkdir $dir | chmod 700 $dir 
fi
if [ $file == $null ]; then 
echo -e "/!\  No file.. Usage: $0 filename ;-) | archive directory - $dir  /!\ "
exit 1
fi
mv $file $dir
$(date "+%H.%d.%m"
).$file
