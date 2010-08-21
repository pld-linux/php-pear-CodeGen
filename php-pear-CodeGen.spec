%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	CodeGen

Summary:	%{_pearname} - Tool to create Code generaters that operate on XML descriptions
Summary(pl.UTF-8):	%{_pearname} - narzędzie do tworzenia generatorów kodu operujących na opisach XML
Name:		php-pear-%{_pearname}
Version:	1.0.6
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	37917a67fd5d6fd0a446994226c251fc
URL:		http://pear.php.net/package/CodeGen
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:5.0
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

%description -l pl.UTF-8
To jest "abstrakcyjny" pakiet udostępniający podstawowy szkielet dla
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
%{php_pear_dir}/%{_pearname}
