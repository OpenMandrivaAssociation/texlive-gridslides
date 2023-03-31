Name:		texlive-gridslides
Version:	54512
Release:	2
Summary:	Free form slides with blocks placed on a grid
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gridslides
License:	lppl1.3 gpl2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gridslides.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gridslides.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows creating free form slides with blocks
placed on a grid. The blocks can be filled with text,
equations, figures etc. The resulting slides are similar to the
ones produced with LaTeX beamer, but more flexible. Sequential
unconvering of elements is supported. A compiler script is
provided which compiles each slide separately, this way
avoiding long compile times.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gridslides
%doc %{_texmfdistdir}/doc/latex/gridslides

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
