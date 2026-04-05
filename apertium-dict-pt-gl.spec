Summary:	Portuguese-Galician language pair for Apertium
Summary(pl.UTF-8):	Para języków portugalski-galicyjski dla Apertium
%define	lpair	pt-gl
Name:		apertium-dict-%{lpair}
Version:	0.9.3
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	https://github.com/apertium/apertium-%{lpair}/archive/v%{version}/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	92f278d4cdbe3dfb17923e5c6466ebef
URL:		https://www.apertium.org/
BuildRequires:	apertium-devel >= 3.7.1
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	pkgconfig
Requires:	apertium >= 3.7.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Portuguese and Galician, morphological analysis or
part-of-speech tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między portugalskim a galicyjskim, a także analizy morfologicznej lub
oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/gl-pt.mode
%{_datadir}/apertium/modes/pt-gl.mode
