#!/bin/tcsh

foreach out ( `ls src/body_*.py` )
    echo $out
    set x = `echo $out | grep -o "src.body_(.*).py"`
    echo $x
end

foreach x ( ops mem btree )
    set out = mongo_$x

end
