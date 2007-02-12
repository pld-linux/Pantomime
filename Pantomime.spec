Summary:	MIME library for GNUstep
Summary(pl.UTF-8):   Biblioteka MIME dla środowiska GNUstep
Name:		Pantomime
Version:	1.1.2
%define cvs 20040729
Release:	5.%{cvs}.2
License:	LGPL
Group:		Libraries
Source0:	%{name}-cvs-%{cvs}.tar.gz
# Source0-md5:	2aa6d2c62181e194c7bf632b720f3fc6
URL:		http://www.collaboration-world.com/pantomime/
BuildRequires:	gnustep-gui-devel >= 0.9.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
MIME library for GNUstep. This framework supports the major mail
protocols: POP3, IMAP, and SMTP.

%description -l pl.UTF-8
Biblioteka MIME dla środowiska GNUstep. Ten szkielet obsługuje główne
protokoły pocztowe: POP3, IMAP i SMTP.

%package devel
Summary:	Header files for Pantomime library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki Pantomime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-gui-devel >= 0.8.8-2
Requires:	openssl-devel >= 0.9.7d

%description devel
Header files for Pantomime library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Pantomime.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Headers/%{libcombo}/Pantomime
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
