## 
## Copyright (c) 2007 - 2014 Joseph Gaeddert
##
## This file is part of liquid.
##
## liquid is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## liquid is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with liquid.  If not, see <http://www.gnu.org/licenses/>.

# 
# liquid-dsp library configure
# Process with autoconf to generate configure script
#

AC_INIT([liquid_dsp],[1.2.0],[support@liquidsdr.org])
AC_CONFIG_SRCDIR([src/libliquid.c])
AC_SUBST([spkg_variation],['v1'])
# permit auxiliary scripts directory (e.g. config.sub, config.guess, install-sh)
AC_CONFIG_AUX_DIR(scripts/)

# Specify 'C' language
AC_LANG(C)

# Autoheader
AH_TEMPLATE([LIQUID_FFTOVERRIDE],  [Force internal FFT even if libfftw is available])

AC_CONFIG_HEADER(config.h)
AH_TOP([
#ifndef __LIQUID_CONFIG_H__
#define __LIQUID_CONFIG_H__
])
AH_BOTTOM([
#endif // __LIQUID_CONFIG_H__
])

# Configure options

AC_ARG_ENABLE(debug,
    AS_HELP_STRING([--enable-debug],[debug]),
    [DEBUG_OPTION="-DDEBUG"],
    [DEBUG_OPTION=""]
)

AC_ARG_ENABLE(profile,
    AS_HELP_STRING([--enable-profile],[profile]),
    [PROFILE_OPTION="-pg"; CLIB="-lc_p"],
    [PROFILE_OPTION="";    CLIB="-lc"]
)

AC_ARG_ENABLE(fftoverride,
    AS_HELP_STRING([--enable-fftoverride],[use internal fft even if libfftw is available]),
    [AC_DEFINE(LIQUID_FFTOVERRIDE)],
    [],
)

AC_ARG_WITH(fec,
    AS_HELP_STRING([--with-fec[=softpkgdir]],[use specified directory as head of fec soft package]),
    [ FEC_ROOT=$withval],
    [ FEC_ROOT=$SDRROOT"/dom/deps/fec_v3"]
)

# Necessary FEC variables
FEC_INCLUDE=" -I"$FEC_ROOT"/cpp/include "
FEC_LIB=" -L"$FEC_ROOT"/cpp/lib "
CPPFLAGS=$CPPFLAGS$FEC_INCLUDE$FEC_LIB
LD_LIBRARY_PATH=$LD_LIBRARY_PATH":"$FEC_ROOT"/cpp/lib"

# Check for necessary programs
AC_PROG_CC
AC_PROG_SED
AC_PROG_GREP
AC_PROG_INSTALL
AC_PROG_RANLIB

# Check for necessary libraries, library functions
AC_FUNC_ERROR_AT_LINE
AC_FUNC_MALLOC
AC_FUNC_REALLOC

# AC_CHECK_LIB (library, function, [action-if-found], [action-if-not-found], [other-libraries])
AC_CHECK_LIB([c],[main], [],[AC_MSG_ERROR(Could not use standard C library)],   [])
AC_CHECK_LIB([m],[main], [],[AC_MSG_ERROR(Could not use standard math library)],[])

# AC_CHECK_FUNC(function, [action-if-found], [action-if-not-found])
AC_CHECK_FUNC([malloc],  [],[AC_MSG_ERROR(Could not use malloc())])
AC_CHECK_FUNC([realloc], [],[AC_MSG_ERROR(Could not use realloc())])
AC_CHECK_FUNC([free],    [],[AC_MSG_ERROR(Could not use free())])
AC_CHECK_FUNC([memset],  [],[AC_MSG_ERROR(Could not use memset())])
AC_CHECK_FUNC([memmove], [],[AC_MSG_ERROR(Could not use memove())])

AC_CHECK_FUNC([sinf],    [],[AC_MSG_ERROR(Could not use sinf())])
AC_CHECK_FUNC([cosf],    [],[AC_MSG_ERROR(Could not use cosf())])
AC_CHECK_FUNC([expf],    [],[AC_MSG_ERROR(Could not use expf())])
AC_CHECK_FUNC([cargf],   [],[AC_MSG_ERROR(Could not use cargf())])
AC_CHECK_FUNC([cexpf],   [],[AC_MSG_ERROR(Could not use cexpf())])
AC_CHECK_FUNC([crealf],  [],[AC_MSG_ERROR(Could not use crealf())])
AC_CHECK_FUNC([cimagf],  [],[AC_MSG_ERROR(Could not use cimagf())])
AC_CHECK_FUNC([sqrtf],   [],[AC_MSG_ERROR(Could not use sqrtf())])

# Check for necessary header files
AC_CHECK_HEADERS([stdio.h stdlib.h complex.h string.h getopt.h sys/resource.h float.h inttypes.h limits.h stdlib.h string.h unistd.h])
if test -z "$HAVE_stdio.h"
then
    AC_MSG_ERROR([Need stdio.h!])
fi

# Check for optional header files, libraries, programs
# Check for fftw
AC_CHECK_HEADERS(fftw3.h)
AC_CHECK_LIB([fftw3f], [fftwf_plan_dft_1d], [],
             [AC_MSG_WARN(fftw3 library useful but not required)],
             [])
# Check for the fec soft package, installed for redhawk
AC_CHECK_HEADERS(fec.h)
AC_CHECK_LIB([fec], [create_viterbi27], [],
             [AC_MSG_WARN(fec library useful but not required)],
             [])

# check for programs (documentation)
AC_CHECK_PROG(PDFLATEX, pdflatex, pdflatex, no)
if [ test "x$PDFLATEX" == "xno" ]; then
    AC_MSG_WARN(pdflatex required to build documentation)
fi
AC_CHECK_PROG(BIBTEX, bibtex, bibtex, no)
if [ test "x$BIBTEX" == "xno" ]; then
    AC_MSG_WARN(bibtex required to build documentation)
fi
AC_CHECK_PROG(EPSTOPDF, epstopdf, epstopdf, no)
if [ test "x$EPSTOPDF" == "xno" ]; then
    AC_MSG_WARN(epstopdf required to build documentation)
fi
AC_CHECK_PROG(GNUPLOT, gnuplot, gnuplot, no)
if [ test "x$GNUPLOT" == "xno" ]; then
    AC_MSG_WARN(gnuplot required to build documentation)
fi
AC_CHECK_PROG(PYGMENTIZE,   pygmentize,     pygmentize,     no)
AC_CHECK_PROG(PYGMENTIZE24, pygmentize-2.4, pygmentize-2.4, no)
if [ test "$PYGMENTIZE" == "no" ]; then
    if [ test "$PYGMENTIZE24" == "no" ]; then
        # use uglier, but functional built-in homebrewed code listing generator
        AC_MSG_WARN(pygmentize not found; using ./scripts/liquid-pygmentize.py as ugly alternative)
        PYGMENTIZE="./scripts/liquid-pygmentize.py"
    else
        PYGMENTIZE="pygmentize-2.4"
    fi
fi


# Checks for typedefs, structures, and compiler characteristics.
AC_C_INLINE
AC_TYPE_SIZE_T
AC_TYPE_UINT32_T
AC_TYPE_UINT8_T

# Check size of certain variables
AC_CHECK_SIZEOF(int)
AC_CHECK_SIZEOF(unsigned int)

# AX_GCC_ARCHFLAG([PORTABLE?], [ACTION-SUCCESS], [ACTION-FAILURE])
# Try to guess the "native" architecture of the target to use with gcc's
# -march or -mtune flags. Default success action adds $ax_cv_gcc_archflag to
# $CFLAGS (sets to "unknown" on failure).
AX_GCC_ARCHFLAG([no],[],[])

# Check canonical system
AC_CANONICAL_TARGET
case $target_cpu in
i386|i486|i586|i686|x86|x86_64)
    # check for MMX/SSE/AVX CPU extensions and intrinsics headers
    #   MMX     :   mmintrin.h
    #   SSE     :   xmmintrin.h
    #   SSE2    :   emmintrin.h
    #   SSE3    :   pmmintrin.h
    #   SSSE3   :   tmmintrin.h
    #   SSE4.1/2:   smmintrin.h
    #   AVX     :   immintrin.h
    AX_EXT
    AC_SUBST([spkg_base], [cpp])

    if [ test "$ax_cv_have_sse41_ext" = yes && test "$ac_cv_header_smmintrin_h" = yes ]; then
        # SSE4.1/2 extensions
        MLIBS_DOTPROD="src/dotprod/src/dotprod_cccf.mmx.o \
                       src/dotprod/src/dotprod_crcf.mmx.o \
                       src/dotprod/src/dotprod_rrrf.mmx.o \
                       src/dotprod/src/sumsq.mmx.o"
    elif [ test "$ax_cv_have_sse2_ext" = yes && test "$ac_cv_header_emmintrin_h" = yes ]; then
        # SSE2 extensions
        MLIBS_DOTPROD="src/dotprod/src/dotprod_cccf.mmx.o \
                       src/dotprod/src/dotprod_crcf.mmx.o \
                       src/dotprod/src/dotprod_rrrf.mmx.o \
                       src/dotprod/src/sumsq.mmx.o"
    else
        # portable C version
        MLIBS_DOTPROD="src/dotprod/src/dotprod_cccf.o \
                       src/dotprod/src/dotprod_crcf.o \
                       src/dotprod/src/dotprod_rrrf.o \
                       src/dotprod/src/sumsq.o"
    fi;;
powerpc*)
    MLIBS_DOTPROD="src/dotprod/src/dotprod_cccf.o \
                   src/dotprod/src/dotprod_rrrf.av.o \
                   src/dotprod/src/dotprod_crcf.av.o \
                   src/dotprod/src/sumsq.o"
    ARCH_OPTION="-fno-common -faltivec";;
arm*)
    # TODO: check for Neon availability

    AC_SUBST([spkg_base], [cpp_arm])
    # ARM architecture : use neon extensions
    MLIBS_DOTPROD="src/dotprod/src/dotprod_cccf.neon.o \
                   src/dotprod/src/dotprod_crcf.neon.o \
                   src/dotprod/src/dotprod_rrrf.neon.o \
                   src/dotprod/src/sumsq.o"
    # TODO: check these flags
    ARCH_OPTION="-marm -mfpu=neon -ftree-vectorize -ffast-math -funsafe-math-optimizations -funsafe-loop-optimizations -ftree-loop-if-convert-stores -mfloat-abi=hard";;
*)
    # unknown architecture : use portable C version
    MLIBS_DOTPROD="src/dotprod/src/dotprod_cccf.o \
                   src/dotprod/src/dotprod_crcf.o \
                   src/dotprod/src/dotprod_rrrf.o \
                   src/dotprod/src/sumsq.o"
    ARCH_OPTION="";;
esac

case $target_os in
darwin*)
    SH_LIB=libliquid_${spkg_variation}.dylib
    REBIND=""
    ;;
*)
    SH_LIB=libliquid_${spkg_variation}.so
    REBIND=ldconfig
    ;;
esac

#
# autoconf variable substitutions
#
AC_SUBST(LIBS)                      # shared libraries (-lc, -lm, etc.)
AC_SUBST(MLIBS_DOTPROD)             # 

AC_SUBST(SH_LIB)                    # output shared library target
AC_SUBST(REBIND)                    # rebinding tool (e.g. ldconfig)
AC_SUBST(ARCH_OPTION)               # compiler architecture option

AC_SUBST(DEBUG_OPTION)              # debug option
AC_SUBST(PROFILE_OPTION)            # profile symbols
AC_SUBST(CLIB)                      # C library linkage (e.g. '-lc')

# documentation programs
AC_SUBST(PDFLATEX)                  # pdflatex
AC_SUBST(BIBTEX)                    # bibtex
AC_SUBST(EPSTOPDF)                  # epstopdf
AC_SUBST(GNUPLOT)                   # gnuplot
AC_SUBST(PYGMENTIZE)                # pygmentize

# "Exporting" the variables to use in the makefile
AC_SUBST(LD_LIBRARY_PATH)
AC_SUBST(FEC_LIB)
AC_SUBST(FEC_INCLUDE)

#Shared package stuff
AC_PREFIX_DEFAULT(${SDRROOT})
#change this number to reflect the variation you are creating for this library
AC_SUBST([spkg_variation], ['v1'])
#name of the impl the package should use
AC_SUBST([OS_NAME],[`uname -s`])
AC_SUBST([ARCH],[`uname -p`])
AC_SUBST([spkg_dir],['${prefix}'/dom/deps/${PACKAGE_NAME}_${spkg_variation}])
AC_SUBST([spkg_impl],[${spkg_base}])
AC_SUBST([spkg_impl2],[${spkg_base}])
AC_SUBST([spkg_lib],[lib])
AC_SUBST([spkg_impldir],['${spkg_dir}/${spkg_impl}'])
AC_SUBST([spkg_libdir],['${spkg_dir}/${spkg_impl}/${spkg_lib}'])
AC_SUBST([spkg_includedir],['${spkg_dir}/${spkg_impl}/include/liquid'])
AC_SUBST([spkg_pkgconfig_dir],[${spkg_libdir}/pkgconfig])

AC_CONFIG_FILES([makefile doc/makefile])
AC_CONFIG_FILES([${PACKAGE_NAME}_${spkg_variation}.pc:packageName.pc.in])
AC_CONFIG_FILES([${PACKAGE_NAME}_${spkg_variation}.spd.xml:packageName.spd.xml.in])
AC_OUTPUT
