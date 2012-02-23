#!/bin/sh

for out in `ls src/body_*.py`
do
    echo $out
    x=${out#src/body_}
    x=${x%.py}
    
    out=mongo_$x

    echo "#!/usr/bin/env python" > $out
    echo "" >> $out
    echo "## GENERATED FILE - DO NOT EDIT" >> $out
    cat src/header.py >> $out
    cat src/body_$x.py >> $out
    cat src/footer.py >> $out
    chmod 755 $out

done
