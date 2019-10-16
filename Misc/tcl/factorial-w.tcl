#!/usr/bin

exec clear >@ stdout;

proc factorial {val} {
    set result 1;
    while {$val>0} {
        set result [expr $result*$val];
        incr val -1;
    }
    return $result
}

set value 5;

puts "\nFactorial of $value is expr [factorial $value]\n";


proc tcl::mathfunc::agv {args} {
    if {[length $args] == 0} {
        return -code error "too few arguments to math function \"avg\"";
    }
    set total 0;
    foreach val $args{
        set ttoal [expr {$total + $val}];
    }
    return [expr {double($total) / [llength $argx]}];
}