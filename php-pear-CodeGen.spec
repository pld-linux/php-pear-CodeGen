%include	/usr/lib/rpm/macros.php
%define		_class		CodeGen
%define		_subclass	%{nil}
%define		_status		beta
%define		_pearname	CodeGen

Summary:	%{_pearname} - Tool to create Code generaters that operate on XML descriptions
Name:		php-pear-%{_pearname}
Version:	1.0.0
%define	_rc rc1
%define	_rel 0.1
Release:	%{_rc}.%{_rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	a05097609f6b8ed42d9acf263c9bb463
URL:		http://pear.php.net/package/CodeGen
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.3
Requires:	php-pear-Console_Getopt >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an 'abstract' package, it provides the base framework for
applications like CodeGen_PECL and CodeGen_MySqlUDF (not released
yet).

In PEAR status of this package is: %{_status}.

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
%{php_pear_dir}/CodeGen/Extension.php
%{php_pear_dir}/CodeGen/XmlParser.php
%{php_pear_dir}/CodeGen/ExtensionParser.php
%{php_pear_dir}/CodeGen/Element.php
%{php_pear_dir}/CodeGen/Release.php
%{php_pear_dir}/CodeGen/Maintainer.php
%{php_pear_dir}/CodeGen/License.php
%{php_pear_dir}/CodeGen/License/PHP.php
%{php_pear_dir}/CodeGen/License/BSD.php
%{php_pear_dir}/CodeGen/License/LGPL.php
%{php_pear_dir}/CodeGen/Command.php
%{php_pear_dir}/CodeGen/Tools/Code.php
%{php_pear_dir}/CodeGen/Tools/Getopt.php
%{php_pear_dir}/CodeGen/Tools/Outbuf.php
%{php_pear_dir}/CodeGen/Tools/Platform.php
%{php_pear_dir}/CodeGen/Tools/Indent.php
%{php_pear_dir}/CodeGen/Tools/Tokenizer.php
%{php_pear_dir}/CodeGen/Tools/FileReplacer.php
