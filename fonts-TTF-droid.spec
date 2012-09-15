Summary:	Droid Fonts family
Name:		fonts-TTF-droid
Version:	0
Release:	4
License:	Apache License
Group:		Fonts
#Source0:	http://download.damieng.com/fonts/redistributed/DroidFamily.zip
Source0:	base-39b04dd27e6d20809f8ff26920d1e761a0005252.tar.gz
# Source0-md5:	db7948a148a065a59c48db27afa16b5d
URL:		http://www.droidfonts.com/
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
The Droid family of fonts was designed by Ascender’s Steve Matteson
beginning in the fall of 2006. The goal was to provide optimal
quality and reading comfort on a mobile handset. The Droid fonts
were optimized for use in application menus, web browsers and for
other screen text.

%prep
%setup -qn base

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

cp -a DroidSans-Bold.ttf	\
      DroidSans.ttf		\
      DroidSansMono.ttf		\
      DroidSerif-*		\
      $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc NOTICE README.txt
%{ttffontsdir}/Droid*.ttf

