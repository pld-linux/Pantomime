# TODO: optflags
%define bver	pre3
Summary:	MIME library for GNUstep
Summary(pl.UTF-8):	Biblioteka MIME dla środowiska GNUstep
Name:		Pantomime
Version:	1.2.0
Release:	0.%{bver}.1
License:	LGPL
Group:		Libraries
Source0:	http://www.collaboration-world.com/cgi-bin/project/download.cgi/%{name}-%{version}%{bver}.tar.gz?rid=109
# Source0-md5:	06ee16477aacf7c5031936997723c791
URL:		http://www.collaboration-world.com/pantomime/
BuildRequires:	gnustep-gui-devel >= 0.9.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes
%{__make} \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} install \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog Documentation/{AUTHORS,README,TODO}
%dir %{_libdir}/GNUstep/Frameworks/Pantomime.framework
%dir %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Pantomime
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Resources
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/Current
#%dir %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/Current/Pantomime
#%dir %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/Current/Resources
#%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/Current/libPantomime.so.1.2.0
%dir %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions
%dir %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/1.2
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/1.2/Resources
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/1.2/Pantomime
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/1.2/libPantomime.so
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/1.2/libPantomime.so.1.2
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/1.2/libPantomime.so.1.2.0
#%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/Resources/English.lproj/Localizable.strings
#%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/Resources/German.lproj/Localizable.strings
%attr(755,root,root)    %{_libdir}/libPantomime.so.1.2.0


%files devel
%defattr(644,root,root,755)
%{_includedir}/Pantomime
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Headers
%dir %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/1.2/Headers
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/1.2/Headers/*.h
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/1.2/Headers/CWIMAPCacheManager.h
%{_libdir}/libPantomime.so
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/libPantomime.so
%{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/Current/libPantomime.so
%dir %{_libdir}/GNUstep/Frameworks/Pantomime.framework/Versions/Current/Headers
