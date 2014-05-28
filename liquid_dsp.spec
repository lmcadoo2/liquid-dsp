#
# This file is protected by Copyright. Please refer to the COPYRIGHT file
# distributed with this source distribution.
#
# This file is part of REDHAWK.
#
# REDHAWK is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# REDHAWK is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#
# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
# You can override this at install time using --prefix /new/sdr/root when invoking rpm (preferred method, if you must)

# Define default SDRROOT
%define _sdrroot    /var/redhawk/sdr
%define _prefix    %{_sdrroot}
#reflects the name in the configure.ac file
Name:		liquid_dsp_v1
#must match the version number in the configure.ac file
Version:	1.0.0
Release:	1%{?dist}
Summary:	The soft package dependency for REDHAWK of the liquid-dsp library
Prefix:		%{_sdrroot}

Group:		Applications/Engineering
License:	GPL
URL:		http://redhawksdr.org/	
Source0:	%{name}-%{version}.tar.gz

AutoReqProv: yes

BuildRequires:	autoconf automake libtool

%if "%{?rhel}" == "6"
Requires: libuuid
BuildRequires: libuuid-devel
%else
Requires: e2fsprogs
BuildRequires: e2fsprogs-devel
%endif

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Liquid-DSP Library for REDHAWK.  Uses version 1.2.0.  
 * Commit: __REVISION__
 * Source Date/Time: __DATETIME__

%package devel
Summary: REDHAWK VITA49 development package
Group: Development/Languages
AutoReqProv: No
Requires: %{name}

%description devel
Development headers and libraries for VITA49 Processing. Uses VITA49 Library version 2759.

%prep
%setup -q


%build
./bootstrap.sh
SDRROOT=%{_sdrroot} %configure
make 


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,redhawk,redhawk)
%dir %{_prefix}/dom/deps/liquid_dsp_v1
%{_prefix}/dom/deps/liquid_dsp_v1/liquid_dsp_v1.spd.xml
%dir %{_prefix}/dom/deps/liquid_dsp_v1/cpp
%dir %{_prefix}/dom/deps/liquid_dsp_v1/cpp/lib
%dir %{_prefix}/dom/deps/liquid_dsp_v1/cpp/lib/pkgconfig/liquid_dsp_v1.pc
%{_prefix}/dom/deps/liquid_dsp_v1/cpp/lib/libliquid_v1.so


%files devel
%defattr(-,redhawk,redhawk)
%dir %{_prefix}/dom/deps/liquid_dsp_v1/cpp
%dir %{_prefix}/dom/deps/liquid_dsp_v1/cpp/include
%{_prefix}/dom/deps/liquid_dsp_v1/cpp/include/liquid.h 
%dir %{_prefix}/dom/deps/liquid_dsp_v1/cpp/lib
%{_prefix}/dom/deps/liquid_dsp_v1/cpp/lib/libliquid_v1.a
%{_prefix}/dom/deps/liquid_dsp_v1/cpp/lib/libliquid_v1.so
%dir %{_prefix}/dom/deps/liquid_dsp_v1/cpp/lib/pkgconfig/
%{_prefix}/dom/deps/liquid_dsp_v1/cpp/lib/pkgconfig/liquid_dsp_v1.pc

