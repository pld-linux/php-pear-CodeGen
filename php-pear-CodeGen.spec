%include	/usr/lib/rpm/macros.php
%define		_class		CodeGen
%define		_subclass	%{nil}
%define		_status		beta
%define		_pearname	CodeGen

%define	_rc rc1
%define	_rel 0.2
Summary:	%{_pearname} - Tool to create Code generaters that operate on XML descriptions
Summary(pl):	%{_pearname} - narzêdzie do tworzenia generatorów kodu operuj±cych na opisach XML
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	%{_rc}.%{_rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	a05097609f6b8ed42d9acf263c9bb463
URL:		http://pear.php.net/package/CodeGen
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:5
Requires:	php-pear
Requires:	php-pear-Console_Getopt >= 1.0
Requires:	php-pear-PEAR-core >= 1:1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an 'abstract' package, it provides the base framework for
applications like CodeGen_PECL and CodeGen_MySqlUDF (not released
yet).

In PEAR status of this package is: %{_status}.

%description -l pl
To jest "abstrakcyjny" pakiet udostêpniaj±cy podstawowy szkielet dla
aplikacji takich jak CodeGen_PECL czy CodeGen_MySqlUDF (jeszcze nie
opublikowanego).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}
