Summary:	replicate stdout into an additional pipeline run in a subshell
Summary(pl):	skieruj kopiê standardowego wyj¶cia do dodatkowego potoku
Name:		tpipe
Version:	1.02
Release:	1
License:	as-is
Group:		Applications/Text
Source0:	http://sources.isc.org/utils/file/%{name}.tar.gz
# Source0-md5:	88d95943087da1c5f144c4acbdbc4869
URL:		http://sources.isc.org/utils/file/tpipe.txt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tpipe is a simple utility program that can be used to split a unix
pipeline into two pipelines. That is, the output of one pipeline can
be replicated and supplied as the input to two other pipelines
executing simultaneously.

%description -l pl
tpipe jest prostym programem narzêdziowym który mo¿e byæ wykorzystany do
rozdzielenia uniksowego potoku do dwóch potoków. To znaczy wyj¶cie jednego
potoku mo¿e byæ rozmna¿ane i dostarczane jako wej¶cie do dwóch innych
potoków wykonywanych równolegle.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install tpipe $RPM_BUILD_ROOT%{_bindir}
install tpipe.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
