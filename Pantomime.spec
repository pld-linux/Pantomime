Summary:	MIME library for GNUstep
Summary(pl):	Biblioteka MIME dla środowiska GNUstep
Name:		Pantomime
Version:	1.1.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.collaboration-world.com/pantomime.data/releases/Stable/%{name}-%{version}.tar.gz
# Source0-md5:	3366a3af44327d03d81cb731da5c1971
Patch0:		%{name}-whitespacepassword.patch
URL:		http://www.collaboration-world.com/pantomime/
BuildRequires:	gnustep-gui-devel >= 0.8.8-2
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
MIME library for GNUstep. This framework supports the major mail
protocols: POP3, IMAP, and SMTP.

%description -l pl
Biblioteka MIME dla środowiska GNUstep. Ten szkielet obsługuje główne
protokoły pocztowe: POP3, IMAP i SMTP.

%package devel
Summary:	Header files for Pantomime library
Summary(pl):	Pliki nagłówkowe biblioteki Pantomime
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gnustep-gui-devel >= 0.8.8-2

%description devel
Header files for Pantomime library.

%description devel -l pl
Pliki nagłówkowe biblioteki Pantomime.

%prep
%setup -q -n %{name}
%patch0 -p1

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
%{_prefix}/System/Library/Headers/%{libcombo}/Pantomime
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
