Summary:	MIME library for GNUstep
Summary(pl):	Biblioteka MIME dla ¶rodowiska GNUstep
Name:		Pantomime
Version:	1.0.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/libs/%{name}-%{version}.tar.gz
# Source0-md5:	-
BuildRequires:	gnustep-gui-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%description
MIME library for GNUstep.

%description -l pl
Biblioteka MIME dla ¶rodowiska GNUstep.

%package devel
Summary:	Header files for Pantomime library
Summary(pl):	Pliki nag³ówkowe biblioteki Pantomime
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gnustep-gui-devel

%description devel
Header files for Pantomime library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Pantomime.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%{__make} -C Bundles/SSL \
	OPTFLAG="%{rpmcflags} -I../../Headers" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%{__make} install -C Bundles/SSL \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%dir %{_prefix}/System/Library/Pantomime
%dir %{_prefix}/System/Library/Pantomime/TCPSSLConnection.bundle
%{_prefix}/System/Library/Pantomime/TCPSSLConnection.bundle/Resources
%attr(755,root,root) %{_prefix}/System/Library/Pantomime/TCPSSLConnection.bundle/%{gscpu}

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Headers/Pantomime
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
