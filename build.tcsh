#!/bin/tcsh

foreach x ( ops mem )
    set out = mongo_$x
    echo "#!"`which python` > $out
    echo "" >> $out
    echo "## GENERATED FILE - DO NOT EDIT" >> $out
    cat src/header.py >> $out
    cat src/body_$x.py >> $out
    cat src/footer.py >> $out
    chmod 755 $out
end
