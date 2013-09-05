Summary:	Rsync libraries
Name:		librsync
Version:	0.9.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/librsync/%{name}-%{version}.tar.gz
# Source0-md5:	24cdb6b78f45e0e83766903fd4f6bc84
Patch0:		%{name}-link.patch
URL:		http://librsync.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files. librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

%package devel
Summary:	Headers for librsync
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files necessary for developing programs
based on librsync.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/rdiff
%attr(755,root,root) %ghost %{_libdir}/librsync.so.?
%attr(755,root,root) %{_libdir}/librsync.so.*.*.*
%{_mandir}/man1/rdiff.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librsync.so
%{_libdir}/librsync.la
%{_includedir}/*
%{_mandir}/man3/*.3*

