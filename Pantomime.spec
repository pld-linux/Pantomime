Summary:	MIME library for GNUstep
Summary(pl.UTF-8):	Biblioteka MIME dla środowiska GNUstep
Name:		Pantomime
Version:	1.2.0
%define bver	pre3
Release:	0.%{bver}.1
License:	LGPL
Group:		Libraries
Source0:	http://www.collaboration-world.com/cgi-bin/project/download.cgi/%{name}-%{version}%{bver}.tar.gz?rid=109
# Source0-md5:	06ee16477aacf7c5031936997723c791
URL:		http://www.collaboration-world.com/pantomime/
BuildRequires:	gnustep-gui-devel >= 0.9.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%description
MIME library for GNUstep. This framework supports the major mail
protocols: POP3, IMAP, and SMTP.

%description -l pl.UTF-8
Biblioteka MIME dla środowiska GNUstep. Ten szkielet obsługuje główne
protokoły pocztowe: POP3, IMAP i SMTP.

%package devel
Summary:	Header files for Pantomime library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Pantomime
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
%doc ChangeLog Documentation/{AUTHORS,README,TODO}
%dir %{_prefix}/System/Library/Frameworks/Pantomime.framework
%{_prefix}/System/Library/Frameworks/Pantomime.framework/Headers
%{_prefix}/System/Library/Frameworks/Pantomime.framework/Resources
%dir %{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions
%dir %{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/A
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/A/libPantomime.so*
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/A/Pantomime
%dir %{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/A/Resources
%{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/A/Resources/*.plist
%{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/A/Resources/English.lproj
%lang(de) %{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/A/Resources/German.lproj
%{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/Current
%dir %{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/Resources
%{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/Resources/English.lproj
%lang(de) %{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/Resources/German.lproj
%attr(755,root,root) %{_prefix}/System/Library/Libraries/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/System/Library/Frameworks/Pantomime.framework/Versions/A/Headers
%{_prefix}/System/Library/Headers/Pantomime
%attr(755,root,root) %{_prefix}/System/Library/Libraries/lib*.so
