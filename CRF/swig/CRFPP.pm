# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.38
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

package CRFPP;
use base qw(Exporter);
use base qw(DynaLoader);
package CRFPPc;
bootstrap CRFPP;
package CRFPP;
@EXPORT = qw();

# ---------- BASE METHODS -------------

package CRFPP;

sub TIEHASH {
    my ($classname,$obj) = @_;
    return bless $obj, $classname;
}

sub CLEAR { }

sub FIRSTKEY { }

sub NEXTKEY { }

sub FETCH {
    my ($self,$field) = @_;
    my $member_func = "swig_${field}_get";
    $self->$member_func();
}

sub STORE {
    my ($self,$field,$newval) = @_;
    my $member_func = "swig_${field}_set";
    $self->$member_func($newval);
}

sub this {
    my $ptr = shift;
    return tied(%$ptr);
}


# ------- FUNCTION WRAPPERS --------

package CRFPP;


# ------- VARIABLE STUBS --------

package CRFPP;

*CRFPP = *CRFPPc::CRFPP;
1;
